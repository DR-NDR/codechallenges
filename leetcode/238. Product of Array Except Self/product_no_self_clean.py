class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        output = []
        zero_exists = 0
        for i,num in enumerate(nums):
            if num !=0:
                total *= num
            else:
                zero_exists += 1
                if zero_exists > 1:
                    return [0]*len(nums)
                zero_index = i
        if zero_exists == 0:
            for num in nums:
                output.append(int(total/num))
        else:
            output = [0]*len(nums)
            output[zero_index] = total
        return output