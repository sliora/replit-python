# 시간복잡도를 nlogn 으로 줄인 two-sum 문제

def twoSum(nums, target):
    nums.sort()
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] + nums[right] > target:
            right -= 1
        elif nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums [right] == target:
            return [left, right]
    return False

print(twoSum(nums=[3,2,4], target=6))


