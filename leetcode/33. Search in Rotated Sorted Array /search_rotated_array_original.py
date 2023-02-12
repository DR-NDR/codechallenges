"""
THIS SOLUTIONS CONSISTS FIRST IN FINDING THE value k and to "re rotate" the array into an array where the numbers are ordered

Then, with an ordered array we search for the needed value, and add the k to find the position in the unordered array

The complexity is O(k*logn * logn) ~ logn
"""

# FIRST BINARY SEARCH
# We look for the value k, which can take any value from 1 to N
# it finds the k, and returns the array without the rotation and the k
def BinSearch_array(nums_original,start,end):
    # first -> first value of the unordered list, it'll help us determine to which k we have to move next
    first = nums_original[0]
    size = len(nums_original)

    # we calculate the k, the equivalent to the mid in a normal binary search
    k = start + (end - start) // 2

    # rotate the array k places 
    new_nums = nums_original[k:size] + nums_original[0:k]

    # when the list is ordered, the first element of it will always be smaller or equal than the last element (in this exercise, there are not duplicate numbers)

    # for example: [0,1,2,3,4], [5], [1,10000]
    if new_nums[0] <= new_nums[size-1]:

        # so if the condition is met, we found the right k and we can return the ordered list
        return new_nums, k

    # if the first we calculated earlier is bigger than the new first element, then the k we used was too big
    # i.e. [4,5,6,7,0,1,2], k=5 -> [1,2,4,5,6,7,0]
    #   first = 4, 4 > 1, so the k needs to be smaller
    elif first > new_nums[0]:
        return BinSearch_array(nums_original,start, k-1)
        
    # if the first we calculated earlier is smaller than the new first element, then the k we used was too small
    # i.e. [4,5,6,7,0,1,2], k=1 -> [5,6,7,0,1,2,4]
    #   first = 4, 4 < 5, so the k needs to be bigger
    elif first < new_nums[0]:
        return BinSearch_array(nums_original,k+1, end)



# SECOND BINARY SEARCH
# NORMAL BINARY SEARCH, looks for a value in a sorted array


# finds the index of an item in a sorted list
def BinSearch_index(nums_sorted, start, end, target):
    mid = start + (end - start) // 2
    if end >= start:
        if nums_sorted[mid] == target:
            return mid

        elif nums_sorted[mid] < target:
            return BinSearch_index(nums_sorted,mid+1, end, target)
        else:
            return BinSearch_index(nums_sorted,start, mid-1, target)
    else:
        return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        original_array, k = BinSearch_array(nums,1,N)

        # rotating a list N places is the same as not rotating, so if k== N, just use it as 0
        k = 0 if N == k else k

        # find the index of the target
        index = BinSearch_index(original_array, 0, N-1, target)
        if index == -1:
            return -1

        # if we go out of bounds, "reset"
        elif index + k >= N:
            return (index+k) - N

        # example: [3,5,1] k=2 -> [1,3,5]
        # the index of 5 in the sorted list is 2, but index + k = 4
        # so we substract the N to stay in bounds
        # index = index + k - N = 2+2-3 = 1

        return index + k 
        
        



