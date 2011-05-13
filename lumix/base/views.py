# Create your views here.

def user_login(request):
    if request.method == 'POST':
        pass
    else:
        render_to_response('login.html')

@login_required
def main(request):
	pass