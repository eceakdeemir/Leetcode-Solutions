class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start = 0
        finish = len(arr) - 1
        while start < finish:
            middle = (start + finish) // 2
            if arr[middle] < arr[middle + 1]:
                start = middle + 1
            elif arr[middle] > arr[middle + 1]:
                finish = middle
        return finish