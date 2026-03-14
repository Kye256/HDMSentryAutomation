import csv, pyodbc
import fileinput

has_top_row = False

def dbase_extract(run_num):
    global has_top_row
    opfile = '../data/results2.csv'
    # Set up the constants
    DRIVER = '{Microsoft Access Driver (*.mdb)}'; PWD = ''

    # Go to the data outputfile for run_num
    database = '../hdmsentry_workspace/%s/WS/RunData/RunData.mdb' %run_num;
    # connect to db
    con = pyodbc.connect('DRIVER={};DBQ={};PWD={}'.format(DRIVER,database,PWD))
    cur = con.cursor()

    # run a query and get the results 

    SQL = 'SELECT Options.OPT_DESC,OptionEconomics.NPV,OptionEconomics.IRR FROM Options INNER JOIN OptionEconomics ON OptionEconomics.OPT_ID = Options.OPT_ID'
    rows = cur.execute(SQL).fetchall()
    SQL = 'SELECT HDM4RunData.DESC FROM HDM4RunData';
    run = cur.execute(SQL).fetchall()
    cur.close()
    con.close()
    named_rows = []
    for row in rows:
        row = list(row)
        row.insert(0,run[0][0])
        row  = tuple(row)
        named_rows.append(row)
    # write the top row of the csv
    if has_top_row == False:
        with open(opfile, 'wb') as output:
            csv_writer = csv.writer(output) # default field-delimiter is ","
            toprow = ['Run Title','Alternative','NPV','IRR']
            csv_writer.writerow(toprow)
            has_top_row = True
    with open(opfile, 'ab') as output:
        csv_writer = csv.writer(output) # default field-delimiter is ","
        csv_writer.writerows(named_rows)
for line in fileinput.input('../data/input2.txt'):
    params = line.split(',')
    try:
        dbase_extract(params[0])
        print '%s' %(params[0]) + "Done"
    except: 
        print '%s' %(params[0]) + "Broken"