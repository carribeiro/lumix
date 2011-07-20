import os
from fabric.api import *
from fabric.contrib.files import exists
from contextlib import contextmanager as _contextmanager
from fabric.contrib.project import rsync_project
from fabric.context_managers import settings, cd, prefix
from fabric.contrib.files import sed

# constants

DEFAULT_PATH_LOCALDEV = '/home/%(user)s/work'
DEFAULT_HOST_LOCALDEV = 'localhost'
DEFAULT_USER_LOCALDEV = env.user

DEFAULT_PATH_SERVER = '/srv'
DEFAULT_HOST_SERVER = '187.1.90.10'
DEFAULT_USER_SERVER = 'lumixadmin'

# globals

env.prj_name = 'lumix' # no spaces!
env.webserver = 'apache2' # nginx or apache2 (directory name below /etc!)
env.dbserver = 'postgresql' # mysql or postgresql
env.user='lumixadmin'

env.dbuser='lumixdb'
env.dbname='lumixdb'
env.dbpassword='luM1Xdb'

# environments
#
# the project can be deployed on two kinds of environment: the localhost is 
# for a local (development) deployment, and the cdnmanager is for a remote 
# server deployment. In both cases, we always set up a single host at a time.
# It does not make sense to deploy the cdnmanager on more than one host.

def localhost(path=DEFAULT_PATH_LOCALDEV, user=DEFAULT_USER_LOCALDEV, 
        host=DEFAULT_HOST_LOCALDEV, createdb=True):
    """ Prepares the local computer, assuming a development setup """
    env.hosts = [host] # always deploy to a single host
    env.user = user
    env.path = path % env  # allows substitution of the %(env.user)s attribute. 
                           # however any attribute in env can be used. we must
                           # check whether this opens a security hole or not, 
                           # depending on what is in the env dictionary
    env.project_path = '%(path)s/%(prj_name)s' % env
    if (os.name == 'nt'):
        env.use_virtualenv = False
    else:
        env.use_virtualenv = True
    if env.use_virtualenv:
        env.virtualenv_path = '%(project_path)s/.env' % env
        env.activate = 'source %(virtualenv_path)s/bin/activate' % env
    env.createdb = createdb

def production(path=DEFAULT_PATH_SERVER, user=DEFAULT_USER_SERVER, 
        host=DEFAULT_HOST_SERVER, createdb=True):
    """ Deploy to a dedicated webserver (can be staging or production) """
    env.hosts = [host] # always deploy to a single host
    env.user = user
    env.path = path # do not perform path substitution on the server.
                    # it's not really needed and it is safer this way.
    env.project_path = '%(path)s/%(prj_name)s' % env
    env.use_virtualenv = True
    if env.use_virtualenv:
        env.virtualenv_path = '%(project_path)s/.env' % env
        env.activate = 'source %(virtualenv_path)s/bin/activate' % env
    env.createdb = createdb

@_contextmanager
def virtualenv():
    with cd(env.project_path):
        with prefix(env.activate):
            yield

def setup():
    """
    Prepare server for the project
    """
 
    sudo('apt-get update')
    sudo('apt-get install gcc python-all-dev libpq-dev git-core -y')
    
    if not exists('/usr/bin/virtualenv',use_sudo=True):
        sudo('apt-get install python-virtualenv -y')
    if not exists('/usr/bin/pip',use_sudo=True):
        sudo('apt-get install python-pip -y')

    if env.hosts[0] == 'localhost':
        pass
    else:
        # install webserver and database server
        with settings(warn_only=True):
            sudo('apt-get remove -y apache2 apache2-mpm-prefork apache2-utils') # is mostly pre-installed
        # install gcc C compiler
        sudo('apt-get install gcc -y')
        if env.webserver=='nginx':
            sudo('apt-get install -y nginx')
        else:
            sudo('apt-get install -y apache2-mpm-worker apache2-utils') # apache2-threaded
            sudo('apt-get install -y libapache2-mod-wsgi') # outdated on hardy!
            sudo('a2enmod wsgi')

    if env.createdb:
        if not exists('/etc/postgresql',use_sudo=True):
            sudo('apt-get install -y postgresql')
        # creates the db user and the database, but doesn't stop on failure, 
        # because these may have been created before
        # TODO: test if the user was created before, and if the db exists, instead of ignoring the error
        with settings(warn_only=True):
            sudo('psql -c "CREATE USER %(dbuser)s WITH NOCREATEDB NOCREATEUSER ENCRYPTED PASSWORD E\'%(dbpassword)s\'"' % env, user='postgres')
            sudo('psql -c "CREATE DATABASE %(dbname)s WITH OWNER %(dbuser)s"' % env, user='postgres')

def resetdb():
    with settings(warn_only=True):
        sudo('psql -c "DROP DATABASE %(dbname)s"' % env, user='postgres')
        sudo('psql -c "CREATE DATABASE %(dbname)s WITH OWNER %(dbuser)s"' % env, user='postgres')
    with virtualenv():
        with cd('%(project_path)s/%(prj_name)s/' % env):
            sudo('./manage.py syncdb --noinput', user=env.user)
            sudo('./manage.py createsuperuser --username=telbrax --email=cribeiro@telbrax.com.br', user=env.user)
            sudo('./manage.py migrate --no-initial-data', user=env.user)
            # cria os arquivos na ordem certa!
            sudo('cat catalogo/sql/produto.sql '+
                 'crm/sql/segmento.sql crm/sql/empresa.sql crm/sql/endereco.sql '+
                 'crm/sql/circuito.sql crm/sql/contrato.sql crm/sql/itemcontrato.sql '+
                 'faturamento/sql/provisaofatura.sql | python manage.py dbshell')

def deploy():
    if env.hosts[0] == 'localhost':
        # create project dir
        if not exists(env.path):
            sudo('mkdir %s' % env.path, user=env.user)

        if not exists(env.project_path):
            local('cd %(path)s && git clone git@github.com:carribeiro/%(prj_name)s.git' % env)
        else:
            local('cd %(path)s && cd %(prj_name)s && git pull' % env)
        
        # create virtualenv
        with cd(env.project_path):
            sudo('virtualenv .env --no-site-packages', user=env.user)
        
        # install packages
        with virtualenv():
            if exists(os.path.join(env.project_path, 'requirements.txt')):
                sudo('pip install -r %(project_path)s/requirements.txt' % env, user=env.user)
            sudo('pip install django-debug-toolbar' % env, user=env.user)
        
        # TODO: don't have these scripts yet, fix it later
        #run('cp %(project_path)s/local_scripts/local_settings_dev.py %(project_path)s/%(prj_name)s/' % env)
        #sudo('mkdir %(project_path)s/%(prj_name)s/uploads' % env,user=env.user)

    # deploy on a remote system
    else:
        # create project dir
        if not exists(env.path):
            sudo('mkdir %s' % env.path,user=env.user)
            sudo('chown %(user)s:%(user)s %(path)s' % env)
    
        sudo('cd %(path)s && git clone git@github.com:carribeiro/%(prj_name)s.git' % env, user=env.user)

        # create virtualenv
        with cd(env.project_path):
            sudo('virtualenv .env --no-site-packages', user=env.user)
        
        # install packages
        with virtualenv():
            sudo('pip install -r %(project_path)s/requirements.txt' % env, user=env.user)
            with cd('%(project_path)s/%(prj_name)s/' % env):
                sudo('./manage.py collectstatic -v0 --noinput', user=env.user)

        # TODO: don't have these scripts yet, fix it later
        #run('cp %(project_path)s/local_scripts/local_settings_prod.py %(project_path)s/%(prj_name)s/' % env)
        #sudo('mkdir %(project_path)s/%(prj_name)s/uploads' % env,user=env.user)

def configure_virtualenv():
        # create virtualenv
        with cd(env.project_path):
            sudo('virtualenv .env --no-site-packages',user=env.user)
        
        # install packages
        with virtualenv():
            sudo('pip install -r %(project_path)s/requirements.txt' % env,user=env.user)

def reload_apache():
    sudo('touch %(project_path)s/%(prj_name)s/django.wsgi' % env)

def configure_wsgi_script():
    if not exists('/etc/apache2/sites-available/%(prj_name)s' % env):
        sudo('cp %(project_path)s/local_scripts/%(prj_name)s /etc/apache2/sites-available/' % env)
        sudo('a2ensite %(prj_name)s' % env)
    run('cp %(project_path)s/local_scripts/django.wsgi %(project_path)s/%(prj_name)s/' % env)    
    sed('%(project_path)s/%(prj_name)s/django.wsgi' % env, '_VIRTUALENVPATH_', '%(virtualenv_path)s' % env)
    sed('%(project_path)s/%(prj_name)s/django.wsgi' % env, '_LUMIXHOME_', '%(project_path)s' % env)

def set_permissions():
    if not exists('%(project_path)s/uploads' % env):
        sudo('mkdir %(project_path)s/uploads' % env)
    sudo('chmod 0777 %(project_path)s/uploads' % env)

def update(update_requirements=False):
    if env.hosts[0] != 'localhost':
        sudo('service apache2 stop')

    with cd(env.project_path):
        # checkout changes
        sudo('git checkout .', user=env.user)
        sudo('git pull', user=env.user)

    with virtualenv():
        with cd('%(project_path)s/%(prj_name)s/' % env):
            sudo('./manage.py collectstatic -v0 --noinput', user=env.user)

    if update_requirements:
        with virtualenv():
            sudo('pip install -U -r %(project_path)s/requirements.txt' % env,user=env.user)

    if env.hosts[0] != 'localhost':
        configure_wsgi_script()

    with virtualenv():
        with cd('%(project_path)s/%(prj_name)s/' % env):
            sudo('./manage.py migrate --no-initial-data', user=env.user)

    set_permissions()
    if env.hosts[0] != 'localhost':
        reload_apache()
        sudo('service apache2 start')
