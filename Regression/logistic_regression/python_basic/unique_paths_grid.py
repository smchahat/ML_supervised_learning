#leet code - https://leetcode.com/problems/unique-paths/description/

m = 3 #row
n = 7 #col

r = [1] * n
col = r * m
l = []
for i in range(m):
    new_List = []
    for j in range(n):
        if (i == 0 and j != 0) or (j == 0 and i > 0):
            new_List.append(1)
        else:
            new_List.append(0)
    l.append(new_List)

for i in l:
    print(i)
for row in range(1, len(l)):
    print("row is :", row)
    #print(len(l[row]))
    for k in range(1, len(l[row])):
        print("values : ", row, k)
        l[row][k] = l[row - 1][k] + l[row][k - 1]
        
#l = ar[m][n]

for i in l:
    print(i)