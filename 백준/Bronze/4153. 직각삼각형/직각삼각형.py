while True:
    nums = list(map(int, input().split()))

    if sum(nums) == 0:
        break

    max_num = max(nums)
    nums.remove(max_num)

    total = nums[0]**2 + nums[1]**2
    result = max_num**2

    if total == result:
        print('right')
    else:
        print('wrong')