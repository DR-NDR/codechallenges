'''
Linear solution - doesnt find the subarray, but finds the sum
basically, each time we find a negative number, reset the current sum

for two reasons: 
    1.- we do not care about negative numbers if they are to be used as sum operands, because they will only make the sum smaller, 
          So while the total sum is still positive, compare it against the max_sum

            for example:
            Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
            Output: 6
            Explanation: [4,-1,2,1] has the largest sum = 6.

            when we reach the number 4, the max_sum will be 4, because the sum reseted when the previous value was negative

            the next iteration, we will add -1, the current sum will still be positive but less than our max_sum
            So the max_sum stays "safe" but we continue with our summing
            the next value will bring the curr_sum to 5, overtaking the current max_sum

            this will keep working, looking for the next values to bring the curr_sum to the max value possible, until an item has a negative value strong enough to turn
            our curr_sum into a negative number, at this point we'll just reset the curr_sum to 0 and start again

    2.- that being said, in an array of all negative numbers, we need to find the 'greatest' one to use it as a subarray of one element
          So, to keep track of the greatest value in a list of all negatives, we should reset the curr_sum after comparing it to the max_sum up until that point
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # set the max to -∞ so that the first comparison sets the first max
        max_sum = float('-inf')
        curr_sum = 0
        for num in nums:
            curr_sum += num
            max_sum = max(max_sum, curr_sum)
            curr_sum = 0 if curr_sum < 0 else curr_sum
        return max_sum
            


