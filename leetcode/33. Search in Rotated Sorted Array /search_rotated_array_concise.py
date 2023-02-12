# i kind of not know how this worked
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        
        while start <= end:
            mid = (start + end) // 2
            
            if nums[mid] == target:
                return mid
            
            # Situation 1:
            # do normal binary search to the left
            if nums[start] <= target <= nums[mid]:
                end = mid - 1
            
            # Situation 2
            # do normal binary search to the right
            elif nums[mid] <= target <= nums[end]:
                start = mid + 1
            
            
            # Situation 3
            # from mid to end, list is sorted
            elif nums[mid] <= nums[end]:
                # if the target is bigger than the right most value
                # or the target is to the left of mid
                if target > nums[end] or target < nums[mid]:
                    # binary search to the left
                    end = mid - 1
            
            # Situation 4
            # from start to mid, list is sorted
            elif nums[start] <= nums[mid]:
                if target > nums[end] or target < nums[mid]:
                    start = mid + 1
                
        return -1
                
            
        
        