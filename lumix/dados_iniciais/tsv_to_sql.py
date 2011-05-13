import sys
import os.path
import re
import decimal
import datetime

IS_PERCENTAGE = re.compile(r'^(-)?[0-9]+(,[0-9]+)?%$')
IS_DECIMAL = re.compile(r'^(-)?[0-9.]+,[0-9]+$')
IS_DATE = re.compile(r'[0-9]+/[0-9]+/[0-9]{1,2}$')
IS_DATE_LONG = re.compile(r'[0-9]+/[0-9]+/[0-9]{1,4}$')

def convert_tsv_to_sql(app_name, model_name, tsvfilename, sqlfilename):

    def convert_field(field):
        if IS_PERCENTAGE.match(field):
            # remove the ending "%" and convert to decimal
            return str(decimal.Decimal(field[:-1].replace(',', '.')).quantize(decimal.Decimal('1.00')))
        elif IS_DECIMAL.match(field):
            # convert to decimal
            return str(decimal.Decimal(field.replace('.','').replace(',', '.')).quantize(decimal.Decimal('1.00')))
        elif IS_DATE.match(field):
            return datetime.datetime.strptime(field, "%d/%m/%y").strftime('%Y-%m-%d')
        elif IS_DATE_LONG.match(field):
            return datetime.datetime.strptime(field, "%d/%m/%Y").strftime('%Y-%m-%d')
        else:
            if len(field) >= 2:
                # retira aspas duplas!
                field = field.replace('"','')
            # duplica aspas simples
            field = field.replace("'","''")
            return field

    with open(sqlfilename, 'w') as sqlfile:
        with open(tsvfilename, 'r') as tsvfile:
            header = tsvfile.readline()
            field_names = [fn.strip() for fn in header.split('\t')]
            sql_field_names = [field_name for field_name in field_names if field_name[-1] != "*" ]
            for row in tsvfile:
                data = ["'%s'" % convert_field(field.strip()) 
                        for field_name, field in zip(field_names, row.split('\t'))]
                sql_data = [(field_name, field) for field_name, field in zip(field_names, data) if ((field_name[-1] != "*") and (field != "''"))]
                print >> sqlfile, "INSERT INTO %s_%s (%s) VALUES (%s);" % (app_name, model_name, ', '.join([x[0] for x in sql_data]), ', '.join([x[1] for x in sql_data]))

if __name__ == "__main__":
    # check if it was called with the correct arguments
    if len(sys.argv) != 3:
        print "Usage: tsv_to_sql <app_name> <model_name>"
        sys.exit(-1)
    # validates arguments
    app_name = sys.argv[1]
    model_name = sys.argv[2]
    tsvfilename = model_name + ".tsv"
    sqlfilename = "../" + app_name + "/sql/" + model_name + ".sql"
    # convert the tsv file
    convert_tsv_to_sql(app_name, model_name, tsvfilename, sqlfilename)
