# Create array 
# http://stackoverflow.com/questions/14676265/how-to-read-text-file-into-a-list-or-array-with-python
import numpy
import fileinput

list_of_lists = []

input_file = '../results/sobol/npvoutput.txt'
for line in fileinput.input(input_file):
    inner_list = [elt.strip() for elt in line.split()]
        # in alternative, if you need to use the file content as numbers
        # inner_list = [int(elt.strip()) for elt in line.split(',')]
    list_of_lists.append(inner_list)
values = numpy.array(list_of_lists)
print values

