import fileinput
import csv

npv = open('C:\Users\Kyeyune.PKAZIBWE-LAP\Documents\Msc. RoadMgtAndEng\Academics\IndividualProject\Analysis\SobolAnalysis\Trial2\\npvOutput.txt', 'w')
for line in fileinput.input('C:\Users\Kyeyune.PKAZIBWE-LAP\Documents\Msc. RoadMgtAndEng\Academics\IndividualProject\Analysis\SobolAnalysis\Trial2\\test.csv'):
    params = line.split(',')
    if params[0] != '0' and params[0] != 'NPV':
        npv.write(params[3]+'\n')

npv.close()

irr = open('C:\Users\Kyeyune.PKAZIBWE-LAP\Documents\Msc. RoadMgtAndEng\Academics\IndividualProject\Analysis\SobolAnalysis\Trial2\\irrOutput.txt', 'w')
for line in fileinput.input('C:\Users\Kyeyune.PKAZIBWE-LAP\Documents\Msc. RoadMgtAndEng\Academics\IndividualProject\Analysis\SobolAnalysis\Trial2\\test.csv'):
    params = line.split(',')
    if params[0] != '0' and params[0] != 'NPV':
        irr.write(params[4]+'\n')
irr.close()
