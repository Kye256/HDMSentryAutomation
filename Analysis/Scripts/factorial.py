import numpy
import fileinput
import csv
import re
import sys

dict_of_dicts = {}

input_file = 'C:\Users\Kyeyune.PKAZIBWE-LAP\Documents\Msc. RoadMgtAndEng\Academics\IndividualProject\Analysis\Scripts\\testinput.txt'

for line in fileinput.input(input_file):
    input_list = line.split(',')
    dict_of_dicts[input_list[0]] = {'TG':input_list[1], 'CO':input_list[2], 'Tv':input_list[3], 'Ge':input_list[4].rstrip('\n')}

output_file = 'C:\Users\Kyeyune.PKAZIBWE-LAP\Documents\Msc. RoadMgtAndEng\Academics\IndividualProject\Analysis\Scripts\\testresults2.csv'

for line in fileinput.input(output_file):
    #run_list = re.findall('T\S*Run\S*',line)
    #run_number = run_list[0]
    output_list = line.split(',')
    run_number = output_list[1].split(' ')[0]
    dict_of_dicts[run_number]['NPV'] = float(output_list[3])
    dict_of_dicts[run_number]['IRR'] = float(output_list[4])
    dict_of_dicts[run_number]['AVE_IRI'] = float(output_list[5].rstrip('\n'))


print sys.getsizeof(dict_of_dicts)
