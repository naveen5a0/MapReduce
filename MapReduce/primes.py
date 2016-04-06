import mincemeat
import time

st_time=time.time()
input_range_data=range(0,1000);
input_data = dict(enumerate(input_range_data))

def mapping_fun(key, val):    
    output_arr=[]
    def prime_check(n):
        if n < 2 or n%2 == 0 and n!=2:
            return False
        if n == 2:
            return True
        else:
            for x in range(3, int(n**0.5)+1, 2):
                if n%x == 0:
                    return False
            return True
    def palin_check(x):
        num = str(x)[::-1]
        return str(x) == num
    
    for i in range(val*10000,(val+1)*10000):
        if prime_check(i) and palin_check(i):
            output_arr.append(i) 
    yield 'number',output_arr

def reduce_fun(keys, vals):
    output_arr=[]
    for i in vals:
        output_arr.extend(i)
    return output_arr

s = mincemeat.Server()
s.datasource = input_data
s.mapfn = mapping_fun
s.reducefn = reduce_fun

output_data = s.run_server(password="changeme")
print "prime number list"
print output_data
print "number of primes"+str(len(output_data['number']))
print("Total time taken for execution of this script : %s seconds" % (time.time() - st_time))