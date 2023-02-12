from collections import deque
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # the intervals aren't sorted
        intervals.sort()

        # to popleft from the queue
        interval_queue = deque(intervals)

        output = []
        
        # to store the "fixed" overlapping interval
        temp_int = []

        # while there are items in the queue
        while interval_queue:
            curr_interval = interval_queue.popleft()

            # if it's the first iteration
            if not temp_int:

                # use the interval as the "main" interval
                temp_int = curr_interval

            # if the intervals overlap
            elif temp_int[1] >= curr_interval[0]:

                # the end of the temp_interval will be whichever is greater between the current_interval and the temp_interval end
                temp_int[1] = max(curr_interval[1], temp_int[1])
            
            # if the intervals don't overlap
            else:

                # add the temp_interval that was built until this point
                output.append(temp_int)

                # update the new temp_interval to the one that didn't overlap
                temp_int = curr_interval

        # at the end, append the last temp_int found
        output.append(temp_int)
        return output
                