class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(len(arr)):
            if arr[i] < arr[i - 1] and i > 0:
                return i - 1