# Python program to read
# json file


import json

# Opening JSON file
fA = open('data_matrikA.json')
fB = open('data_matrikB.json')
# returns JSON object as
# a dictionary
dataA = json.load(fA);
dataB = json.load(fB);

# Iterating through the json
# list

print ("tampil data Matrik A") ;   
for i in dataA['matrik_A']:
	print(i);
    
print ("tampil data Matrik B") ;   
for i in dataB['matrik_B']:
	print(i);
# Closing file
fA.close()
fB.close()
