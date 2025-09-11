s1 = "anagram"
s2 = "grammar"

count = 0
dict = {}
k = 2
for i in s1:
    if not dict:
        dict[i] = 1
    elif i in dict:
        dict[i] = dict[i] + 1
    else:
        dict[i] = 1
print(dict)

for j in s2:
    
    if j in dict:
        dict[j] = dict[j]-1
    else :
        count = count+1

    if j in dict and dict[j] == 0:
        del dict[j]

if count == k:
    print("True")

print(dict, count)