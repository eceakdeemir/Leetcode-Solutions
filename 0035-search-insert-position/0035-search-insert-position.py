class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        last = len(nums) - 1
        while (start <= last):
            middle = (start + last) // 2
            if nums[middle] < target:
                start = middle + 1
            elif nums[middle] > target:
                last = middle - 1
            else:
                return middle
        return start