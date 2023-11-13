nums = [3,1,2,10,1]
results = [0]*len(nums)
results[0]= nums[0]
print(results)
for i in range(1,len(nums)):
    results[i] = nums[i]+results[i-1]
    print(results)
print(results)


