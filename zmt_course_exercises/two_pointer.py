def two_sum(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return [nums[left], nums[right]]

        elif current_sum < target:
            left += 1

        else:
            right -= 1

    return None

def three_sum(nums):
    nums.sort()
    result = []

    for i in range(len(nums)):
        left, right = i + 1, len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1

    return result


arr = [2, 7, 5, 1, 9, -3, -1, -2]
print(three_sum(arr))