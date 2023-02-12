'''
brute force approach
O(N^2) with big numbers it exceeds the time limit
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        max_prod = float('-inf')
        for i in range(N):
            for j in range(i,N):
                if i == j:
                    product = nums[i]
                    max_prod = max(max_prod,product)
                else:
                    product *= nums[j]
                    max_prod = max(max_prod,product)
        return max_prod
            
