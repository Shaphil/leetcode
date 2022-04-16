def arrayPairSum(nums):
    nums.sort()
    total = 0
    for i in range(0, len(nums), 2):
        total += nums[i]
    
    return total


if __name__ == "__main__":
    a = [1, 4, 3, 2]
    max_sum = arrayPairSum(a)
    print(max_sum)
