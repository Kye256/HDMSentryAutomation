import csv, pyodbc
import fileinput

# Gets the results (NPV and IRR) of HDM SENTRY runs and Outputs them in results2.csv file
# Includes a test for which analyses were done and record of which analyses failed in failedruns.txt

has_top_row = False # Variable to check if the output file has been created and a top row inserted

def dbase_extract(run_num):
    global has_top_row  
    
    opfile = './data/results2test.csv'
    # Set up the constants
    DRIVER = '{Microsoft Access Driver (*.mdb)}'; PWD = ''

    # Go to the data outputfile for run_num
    database = './hdmsentry_workspace/%s/WS/RunData/RunData.mdb' %run_num;
    # connect to db
    con = pyodbc.connect('DRIVER={};DBQ={};PWD={}'.format(DRIVER,database,PWD))
    cur = con.cursor()

    # run a query and get the results 

    SQL = 'SELECT Options.OPT_DESC,OptionEconomics.NPV,OptionEconomics.IRR,SectOptData.IRIAV FROM Options,OptionEconomics,SectOptData WHERE OptionEconomics.OPT_ID = Options.OPT_ID and SectOptData.OPT_ID = Options.OPT_ID'
    rows = cur.execute(SQL).fetchall()
    SQL = 'SELECT HDM4RunData.DESC FROM HDM4RunData';
    run = cur.execute(SQL).fetchall()
    cur.close()
    con.close()
    named_rows = []
    # Create a list of tuples in named_rows. Each tuple contains a row of data to be written in the output file
    for row in rows:
        row = list(row)
        row.insert(0,run[0][0])
        row  = tuple(row)
        named_rows.append(row)
    # write the top row of the csv
    if has_top_row == False:
        with open(opfile, 'wb') as output:
            csv_writer = csv.writer(output) # default field-delimiter is ","
            toprow = ['Run Title','Alternative','NPV','IRR','AVE_IRI']
            csv_writer.writerow(toprow)
            has_top_row = True
    with open(opfile, 'ab') as output:
        csv_writer = csv.writer(output) # default field-delimiter is ","
        csv_writer.writerows(named_rows)
dmp = open('./data/failedrunsTest.txt', 'wb')
for line in fileinput.input('./data/input2.txt'):
    params = line.split(',')
    try:
        dbase_extract(params[0])
        print '%s' %(params[0]) + "Done"
    except: 
        print '%s' %(params[0]) + "Broken"
        dmp.write('%s' %(params[0]) + "Broken" + "\r\n")
dmp.close()