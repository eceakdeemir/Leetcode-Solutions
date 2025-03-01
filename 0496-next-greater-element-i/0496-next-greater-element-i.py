class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hash_table = {}

        for i in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] < nums2[i]:
                stack.pop()
            hash_table[nums2[i]] = stack[-1] if stack else -1
            stack.append(nums2[i])
        return [hash_table[num] for num in nums1]