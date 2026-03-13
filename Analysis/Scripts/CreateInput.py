import itertools

input_list = [[1,2,3,4],[0,1,2,3,4],[0,1,2],[0,1,2,3,4,5,6]] # Order is [ [Traffic_Growth, Condition, Traffic_volume, Geometry]]
inputs = list(itertools.product(*input_list))

fh = open('C:\Users\Kyeyune.PKAZIBWE-LAP\Documents\Msc. RoadMgtAndEng\Academics\IndividualProject\Analysis\Scripts\\input7.txt', 'w')
run_number = 1

for item in inputs:
    output = "T7Run%s," %run_number +str(item[0])+","+str(item[1])+","+str(item[2])+","+str(item[3])+"\n"
    run_number += 1
    fh.write(output)
fh.close()