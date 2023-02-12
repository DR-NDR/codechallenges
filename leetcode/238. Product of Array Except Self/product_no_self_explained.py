"""
Given an integer array nums,
return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]

example: 
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # start the "accumulator" at 1
        total = 1

        output = []

        # flag / counter in case there's a zero
        zero_exists = 0

        for num in nums:
            if num !=0:
                # then we can multiply and accumulate it
                total *= num
            else:
                # if num is 0, do not "ruin" the total, just keep in mind there's a zero now
                zero_exists += 1

                 # if there are more than 1 zeros, that means that the product will always be 0
                if zero_exists > 1:
                    return [0]*len(nums)

        # if there is only one zero or none at all, iterate
        for num in nums:

            # if there's a zero somewhere on the list, but not in the current number
            if zero_exists and num != 0:

                # then the current number will multiply itself with 0, so add the 0 to the result
                output.append(0)

            # if the current number is zero, from zero_exists <= 1, we know that it is the only zero
            elif num == 0:

                # so output the total
                output.append(total)

            else:
                # if there aren't zeros, append the total divided by the current number
                output.append(int(total/num))            
        return output