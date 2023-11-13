nums = [3,1,2,10,1]
print(nums)
for i in range(1,len(nums)):
    nums[i] = nums[i -1] + nums[i]
print(nums)


