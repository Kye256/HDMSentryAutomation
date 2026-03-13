# Similar to the factorial01 but uses a list of dictionaries instead of dictionary of dictionaries to store the data in memory

import numpy
import fileinput
import csv
import re
import sys

list_of_dicts = [None] # Initialize list with None to allow the run numbers to align with the list index

input_file = 'C:\Users\Kyeyune.PKAZIBWE-LAP\Documents\Msc. RoadMgtAndEng\Academics\IndividualProject\Analysis\Scripts\\testinput.txt'

for line in fileinput.input(input_file):
    input_list = line.split(',')
    run_number = int(re.findall('(?<=Run)\d*', input_list[0])[0]) # RegEx finds the run number returns list and first item of the list is cast into an int for use as run_number
    list_of_dicts.insert(run_number, {'Run':input_list[0], 'TG':input_list[1], 'CO':input_list[2], 'Tv':input_list[3], 'Ge':input_list[4].rstrip('\n')})  # Inserts the dictionary at the run_number index of the list
    #print list_of_dicts[run_number], run_number, '\n'

output_file = 'C:\Users\Kyeyune.PKAZIBWE-LAP\Documents\Msc. RoadMgtAndEng\Academics\IndividualProject\Analysis\Scripts\\testresults2.csv'

for line in fileinput.input(output_file):
    output_list = line.split(',')
    run_number = int(re.findall('(?<=Run)\d*', output_list[1])[0])
    list_of_dicts[run_number]['NPV'] = float(output_list[3]) # This picks the NPV value which is in the 4th row of the CSV. Edit to suit format of CSV file
    list_of_dicts[run_number]['IRR'] = float(output_list[4])
    list_of_dicts[run_number]['AVE_IRI'] = float(output_list[5].rstrip('\n'))
   
print list_of_dicts[0]

n = 0
for run in list_of_dicts:
    if 
    