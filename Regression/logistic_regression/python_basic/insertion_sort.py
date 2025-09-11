insert = [4,2,1,3]

print("insert : ", insert) 
for i in range(1, len(insert)):
    j = 0
    while i > j:
        if insert[i] < insert[j]:
            insert[j], insert[i] = insert[i], insert[j]
        j += 1
     
print("insert : ", insert)  