'''
brute force solution, checks all the possible subarrays and compares the sums
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        max_sum = nums[0]
        for i in range(N):
            # if number is negative it only helps to sum it if it's greater than the current max sum
            if nums[i] < 0 and nums[i] < max_sum:
                continue
            # build all the subarrays starting in i
            for j in range(i,N+1):
                summ = sum(nums[i:j+1])
                max_sum = max(max_sum,summ)
        return max_sum
