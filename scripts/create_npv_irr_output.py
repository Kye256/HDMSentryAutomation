import fileinput
import csv

npv = open('../results/sobol/npvOutput.txt', 'w')
for line in fileinput.input('../results/sobol/test.csv'):
    params = line.split(',')
    if params[0] != '0' and params[0] != 'NPV':
        npv.write(params[3]+'\n')

npv.close()

irr = open('../results/sobol/irrOutput.txt', 'w')
for line in fileinput.input('../results/sobol/test.csv'):
    params = line.split(',')
    if params[0] != '0' and params[0] != 'NPV':
        irr.write(params[4]+'\n')
irr.close()
