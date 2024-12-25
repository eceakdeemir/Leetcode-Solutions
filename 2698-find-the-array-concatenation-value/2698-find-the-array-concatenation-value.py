class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        total = 0
        if (len(nums) % 2 != 0):
            total = nums[len(nums) // 2]
        for i in range(len(nums) // 2):
            total += int(str(nums[i]) + str(nums[len(nums) - 1 - i]))
        return (total)