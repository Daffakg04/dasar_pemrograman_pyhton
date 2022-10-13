import numpy as np;
matrik_a = np.array([[1, 5, 6],[4, 2, 1],[0, 0, 1]])
matrik_c = np.array([])
#mencari ordo 3 x 3
print(matrik_a.shape)
print(matrik_a)


print("=============================================\n")


print("==========matrik 2x2==========================\n")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)

print(newarr)

print("==========matrik 1x3==========================\n")

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(2,3,-1)

print(newarr)

print("==========penjumlahan ==========================\n")
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x+x)

print("==========pengurangan==========================\n")
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x-x)