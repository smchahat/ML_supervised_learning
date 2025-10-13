nums = [3,1,-2,-5,2,-4]

length = len(nums)
res = [0] * length

i = 0
j = 1

for k in range(length):
    if nums[k] > 0:
        res[i] = nums[k]
        i = i+2
    if nums[k] < 0:
        res[j] = nums[k]
        j = j+2

        
print(res)
