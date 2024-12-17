class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first = {}
        last = {}
        count = {}
        degree = 0
        for i, x in enumerate(nums):
            if not x in count:
                first[x] = i
                count[x] = 0
            last[x] = i
            count[x] += 1
            degree = max(degree, count[x]) 
        lensub = float('inf')
        for x in count:
            if count[x] == degree:
                lensub = min(abs(first[x] - last[x]) + 1, lensub)
        return (lensub)