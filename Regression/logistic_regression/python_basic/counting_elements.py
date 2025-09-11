arr = [1, 2, 3]

#output = 2
arr = [1,1,3,3,5,5,7,7]
arr = [1,3,2,3,5,0]
arr = [1,1,2,2]

s = set(arr)

counter = 0
for i in arr:
    if (i+1) in s:
        counter += 1

print(counter)