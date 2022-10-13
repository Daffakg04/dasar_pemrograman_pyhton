import numpy as np;
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr)
print("================menentukan deatil array==================")
print(newarr[0,0,0])
print(newarr[0,0,1])
print(newarr[0,1,0])
print(newarr[0,1,1])
print(newarr[0,2,0])
print(newarr[0,2,1])

print(newarr[1,0,0])
print(newarr[1,0,1])
print(newarr[1,1,0])
print(newarr[1,1,1])
print(newarr[1,2,0])
print(newarr[1,2,1])

print("================pencarian array===================")

arr2 = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr2 == 4)

print(x)
   
