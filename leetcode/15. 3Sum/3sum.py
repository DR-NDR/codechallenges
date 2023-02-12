def threeSum(self, nums):
    res = []

    # sort for an easier iteration, we only care about the values, not the indices
    nums.sort()

    # iterate the list without taking the last 2 values, those will get taken care of by the pointers left and right in the last iteration
    for i in xrange(len(nums)-2):

        # since the list can have repeated numbers, whenever we find a repetition, skip any anaylisis and just 'continue' 
        # this repetition can only hapen after the first iteration
        if i > 0 and nums[i] == nums[i-1]:
            continue

        # l -> left pointer
        # r -> right pointer

        # l will point to the item next to the current item
        # r will point to the last value
        l, r = i+1, len(nums)-1

        # while the left pointer is to the left of the right
        while l < r:

            # check the sum of the current values in i,l and r
            s = nums[i] + nums[l] + nums[r]

            # if the sum is negative, the left pointer may be the one causing it, so advance it
            if s < 0:
                l +=1 

            # if the sum is positive, the righter value may be too high, decrese the pointer
            elif s > 0:
                r -= 1

            # sum is 0
            else:
                res.append((nums[i], nums[l], nums[r]))

                # to continue with the first while, we have to make sure that the value of the left pointer isn't repeated
                while l < r and nums[l] == nums[l+1]:

                    # if it is repeated, advance the l pointer until they are different
                    l += 1

                # also make sure the right pointer is not repeated
                while l < r and nums[r] == nums[r-1]:
                    # if it is repeated, keep moving the r pointer to the left until it isn't repeating itself
                    r -= 1

                # move the pointers to the next values
                l += 1; r -= 1
    return res