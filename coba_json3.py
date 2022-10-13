# Python program to read
# json file


import json

# Opening JSON file
f = open('data.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
print ("NIP");
print ("=====") ;   
for i in data['emp_karyawan']:
	#print(i);
    print(i["NIP"]) ;

# Closing file
f.close()
