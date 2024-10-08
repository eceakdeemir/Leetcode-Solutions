def func(capability, k, nums):
    count = 0
    i = 0
    while (i < len(nums)):
        if nums[i] <= capability:
            count += 1
            i += 2
        else:
            i += 1
    return count >= k

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        minimum = min(nums)
        maximum = max(nums)
        mid = (minimum + maximum) // 2

        while minimum < maximum:
            mid = (minimum + maximum) // 2
            if func(mid, k, nums):
                maximum = mid
            else:
                minimum = mid + 1
        return minimum
        
