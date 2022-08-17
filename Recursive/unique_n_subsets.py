nums = [1,2,2,2,3,4,5]

for i in range(0, len(nums)):
    if i == 0 or nums[i-1] != nums[i]:
        for j in range(i+1, len(nums)):
            if j == i+1 or nums[j-1] != nums[j]:
                for k in range(j+1, len(nums)):
                    if k == j+1 or nums[k-1] != nums[k]:
                        print(nums[i], nums[j], nums[k])