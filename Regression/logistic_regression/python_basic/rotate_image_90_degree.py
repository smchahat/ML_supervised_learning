matrix = [[1,2,3],[4,5,6],[7,8,9]]
#matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
arr_size = len(matrix)

for i in range(arr_size):
  for j in range(i, arr_size):
    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

print(matrix)
for i in range(arr_size):
  last = arr_size - 1
  for j in range(int(arr_size/2)):
    #print("j : ", j)
    matrix[i][j], matrix[i][last] = matrix[i][last], matrix[i][j]
    last -= 1

print(matrix)
