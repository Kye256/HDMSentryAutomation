import numpy
import fileinput
from SALib.analyze import ff, ff_test
from SALib.analyze import morris

# Based on the example in the SALib documentation http://salib.readthedocs.io/en/latest/basics.html
# Define problem
# Or if we are using a file we use 
"""
There are two ways of definging a problem. This one and the one which is not commented out 
Decide which method to use and comment out the other. 

from SALib.util import read_param_file
problem = read_param_file('/path/to/file.txt')
"""

problem = {
    'num_vars': 4,
    'names': ['TG', 'Co', 'Tv', 'Ge'],
    'groups': None,
    'bounds': [[1, 4],
               [0, 4],
               [0, 2],
               [0, 6]]
}


# Read the inputs and create a numpy matrix with them
input_file = 'C:\Users\Kyeyune.PKAZIBWE-LAP\Documents\Msc. RoadMgtAndEng\Academics\IndividualProject\Analysis\SobolAnalysis\Trial2\\rawInput.txt'
input_list_of_lists = []
output_list_of_lists = []

for line in fileinput.input(input_file):
    inner_list = [int(elt.strip()) for elt in line.split(',')]
        # in alternative, if you need to use the file content as numbers
        # inner_list = [int(elt.strip()) for elt in line.split(',')]
    input_list_of_lists.append(inner_list)

in_values = numpy.array(input_list_of_lists)

X  = in_values.T    # Try to transpose to deal with the error given by the dot product later on. Remove this comment once code is working

# Read the outputs and create a numpy array with them
output_file = 'C:\Users\Kyeyune.PKAZIBWE-LAP\Documents\Msc. RoadMgtAndEng\Academics\IndividualProject\Analysis\SobolAnalysis\Trial2\\npvoutput.txt'


for line in fileinput.input(output_file):
    inner_list = [int(elt.strip()) for elt in line.split(',')]
        # in alternative, if you need to use the file content as numbers
        # inner_list = [int(elt.strip()) for elt in line.split(',')]
    output_list_of_lists.append(inner_list)

op_values = numpy.array(output_list_of_lists)
print type(op_values)
print op_values.shape
# Pass the inputs and outputs array to the chosen analyse function

print numpy.dot(X, op_values)

morris.analyze(problem, in_values, op_values, print_to_console=True)
ff_test.analyze(problem, X, op_values, print_to_console=True)
'''print "This is the value of X:"  
print (ff_test.analyze(problem, in_values, op_values, print_to_console=True))'''
# Present the results of the output analysis

