nums = [10,9,2,5,3,7,101,18]
#      [0, 1,2,3,4,5,6  ,7]
length = len(nums)
l = [1] * (length )

print(length)
for i in range(length - 2, -1,-1):
    for j in range(i, length-1):
        if nums[i] < nums[j+1]:
            l[i] = max(l[i], 1 +l[j+1])

print(max(l))