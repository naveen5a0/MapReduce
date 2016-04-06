import mincemeat
import sys
import hashlib
import time

st_time=time.time()
enum_data=[]
input_data={}
hex_input = sys.argv[1]

def custom_enum(enum_len, pos_outcomes):
  res = []
  if enum_len == 1:
    return list(pos_outcomes)
  else:
    sub_out = custom_enum(enum_len -1, pos_outcomes)
    for k in pos_outcomes:
      for s in sub_out:
        res.append(str(k) + str(s))
  return res

enum_data=custom_enum(1,"abcdefghijklmnopqrstuvwxyz0123456789")+custom_enum(2,"abcdefghijklmnopqrstuvwxyz0123456789")+custom_enum(3,"abcdefghijklmnopqrstuvwxyz0123456789")+custom_enum(4,"abcdefghijklmnopqrstuvwxyz0123456789")


temp = ''
count = 0
for line in enum_data:
  temp = temp + line.rstrip() + ' '
  if count % 100000 == 0:
    temp = temp + hex_input
    input_data[count] = temp
    temp = ''
  count += 1
  
input_data[count] = temp

def mapping_fun(key,val):
 map_arr={}
 import md5
 split_val=val.split()
 a=split_val[-1]
 for map_arr in split_val:
   map_arr=map_arr.strip()
   hash_str=md5.new(map_arr).hexdigest()
   if hash_str[:5]==a:
     yield map_arr,a

def reducefn(keys,vals):
	return vals



s=mincemeat.Server()
s.datasource = input_data
s.mapfn = mapping_fun
s.reducefn =reducefn

output_data = s.run_server(password="changeme")
print "found the possibilities"
print output_data.keys()
print("Total time taken for execution of this script : %s seconds" % (time.time() - st_time))