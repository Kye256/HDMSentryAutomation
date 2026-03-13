import csv, pyodbc

# set up some constants. Note that the DB path here is for test purposes.
MDB = 'C:\Users\Kyeyune.PKAZIBWE-LAP\Documents\HDMSentry\ww\WS\RunData\RunData.mdb'; DRV = '{Microsoft Access Driver (*.mdb)}'; PWD = 'pw'

# connect to db
con = pyodbc.connect('DRIVER={};DBQ={};PWD={}'.format(DRV,MDB,PWD))
cur = con.cursor()

# run a query and get the results 
#SQL = 'SELECT OptionEconomics.NPV,OptionEconomics.IRR,OptionEconomics.OPT_ID FROM OptionEconomics ;' # query the results from HDM-4 for NPV and IRR
SQL = 'SELECT Options.OPT_DESC,OptionEconomics.NPV,OptionEconomics.IRR FROM Options INNER JOIN OptionEconomics ON OptionEconomics.OPT_ID = Options.OPT_ID;'
rows = cur.execute(SQL).fetchall()
cur.close()
con.close()

# you could change the mode from 'w' to 'a' (append) for any subsequent queries
with open('C:\Users\Kyeyune.PKAZIBWE-LAP\Documents\HDMSentry\ww\WS\RunData\\test.csv', 'w') as output:
    csv_writer = csv.writer(output) # default field-delimiter is ","
    toprow = ['Alternative','NPV','IRR']
    csv_writer.writerow(toprow)
    csv_writer.writerows(rows)