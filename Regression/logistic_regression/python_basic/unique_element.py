arr = [1,2,1,5,5]

#find unique number without using dict


ans = 0

for items in arr:
    ans ^= items

print(ans)