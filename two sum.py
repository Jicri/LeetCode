def two_sum(nums):
    target = 15
    #sum_num = None
    for i in range(len(nums)):
        for j in range(len(nums)):
            if j > i:
                sum_num = nums[i] + nums[j]
                if sum_num == target:
                    print(i, j)


two_sum([4, 7, 8, 7, 11])
