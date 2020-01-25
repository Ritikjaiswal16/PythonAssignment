matrix=[[2,3,4,5,3,1],[5,6,4,3,2,7]]
flat=[i for j in matrix for i in j if i>3]
print(flat)
