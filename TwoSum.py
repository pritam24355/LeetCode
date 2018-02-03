class Solution(object):
   
    def twoSum(self, nums, target):
        count=1
        length=len(nums)
        print target
        for n in range(len(nums)):
            l1=nums[n]
            if target-l1 in nums and nums.index(target-l1)!=n:
                
                print n,nums.index(target-l1)
                return [n,nums.index(target-l1)]
            