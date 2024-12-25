class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        total = 0
        while len(nums) > 0:
            if len(nums) > 1:
                total += int(str(nums[0]) + str(nums[-1]))
                del nums[-1]
            else:
                total += nums[0]
            del nums[0]
        return (total)