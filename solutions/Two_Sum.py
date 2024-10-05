class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = {}
        for i in range(len(nums)):
            number = target - nums[i]
            if number in arr:
                return [arr[number], i]
            arr[nums[i]] = i