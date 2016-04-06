import mincemeat
import sys
import time
#recording the intitial starting time
st_time = time.time()

#opening the input file in read mode and saving into file_input variable
file=open(str(sys.argv[1]),'r')
file_input = list(file)
file.close()

input_data_dict = dict(enumerate(file_input))

def mapping_fun(key,val):
    for i in val.split():
        #print n
        yield '1',float(i)


def reduce_fun(keys,vals):
    import math
    input_sum = sum(vals)
    input_mean = sum(vals)/len(vals)
    input_sd = 0
    for i in vals:
        input_sd = input_sd + ((input_mean-i)*(input_mean-i)) 
    input_sd = input_sd/len(vals)
    return ['input sum : '+str(input_sum), 'length :'+str(len(vals)), 'standard_deviation :'+str(math.sqrt(input_sd))]

s=mincemeat.Server()
s.datasource = input_data_dict
s.mapfn = mapping_fun
s.reducefn = reduce_fun

output_data = s.run_server(password="changeme")
#print output_data
for i in output_data:
    for k in output_data.get(i):
        print k
print("Total time taken for execution of this script : %s seconds" % (time.time() - st_time))


