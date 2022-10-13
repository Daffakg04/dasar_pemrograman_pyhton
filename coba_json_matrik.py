# Python program to read
# json file


import json

# Opening JSON file
f = open('data_matrik.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list

print ("tampil data dari data JSON") ;   
for i in data['matrik_A']:
	print(i);
    

# Closing file
f.close()
