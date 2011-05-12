import sys
import os.path
import re
import decimal

IS_PERCENTAGE = re.compile(r'^(-)?[0-9]+(,[0-9]+)?%$')
IS_DECIMAL = re.compile(r'^(-)?[0-9]+(,[0-9]+)?%$')

def convert_csv_to_sql(app_name, model_name, csvfilename, sqlfilename):

    def convert_field(field):
        if IS_PERCENTAGE.match(field):
            # remove the ending "%" and convert to decimal
            return str(decimal.Decimal(field[:-1].replace(',', '.')).quantize(decimal.Decimal('1.00')))
        elif IS_DECIMAL.match(field):
            # convert to decimal
            return str(decimal.Decimal(field.replace(',', '.')).quantize(decimal.Decimal('1.00')))
        else:
            return field

    with open(sqlfilename, 'w') as sqlfile:
        with open(csvfilename, 'r') as csvfile:
            header = csvfile.readline().strip()
            field_names = ', '.join(header.split(';'))
            for row in csvfile:
                data = ', '.join(["'%s'" % convert_field(field.strip()) for field in row.split(';')])
                print >> sqlfile, "INSERT INTO %s_%s (%s) VALUES (%s);" % (app_name, model_name, field_names, data)

if __name__ == "__main__":
    # check if it was called with the correct arguments
    if len(sys.argv) != 3:
        print "Usage: csv_to_sql <app_name> <model_name> | <csv_file_name> (where the csv_file_name is model_name+'.csv'>"
        sys.exit(-1)
    # validates arguments
    app_name = sys.argv[1]
    csvfilename = sys.argv[2]
    basefilename, csv_ext = os.path.splitext(csvfilename)
    basedir, model_name = os.path.split(basefilename)
    if csv_ext == '':
        csvfilename = basefilename + ".csv"
    sqlfilename = basefilename + ".sql"
    # convert the csv file
    convert_csv_to_sql(app_name, model_name, csvfilename, sqlfilename)