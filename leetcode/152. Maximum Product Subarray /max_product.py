'''
best solution is to iterate the list once
it's not enough one variable to keep track of the max product, 
    because a negative number will turn it to a negative value 
    and we do not know how many negative numbers there are
at the same time, the negative number will also turn other negative numbers into positive bigger numbers
    so, we need to use another variable to store the smallest product, in case we can multiply it later 
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # temp_max is a temporary max, result is the actual max
        result = temp_max = minn = nums[0]
        for i in range(1,len(nums)):
            number = nums[i]

            # if number is negative switch the min and max
            if number < 0 :
                temp_max, minn = minn, temp_max
            
            temp_max *= number 
            minn *= number
            
            # find the max 
            temp_max = max(temp_max,number)

            # find the min 
            minn = min(minn,number) 

            # if the temp_max we found is the maximum value so far, update it    
            result = max(temp_max, result)
        return result
                
            


