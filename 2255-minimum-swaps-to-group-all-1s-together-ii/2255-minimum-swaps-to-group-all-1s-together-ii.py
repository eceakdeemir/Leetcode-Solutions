class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        len_num = len(nums)
        one = sum(nums)

        if one == 0 or one == len_num:
            return 0
        current = sum(nums[:one])
        maxi = current

        for i in range(len_num):
            current -= nums[i]
            current += nums[(i + one) % len_num]
            maxi = max(maxi, current)
        return one - maxi