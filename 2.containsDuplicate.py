class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # brute force  O(n^2)
        # for i in range(0, len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if  i != j and nums[i] == nums[j]:
        #             return True
        # return False

        # time complexity : o(n.logn())
        # nums.sort() 
        # p1, p2= 0, 1
        # while(p2 < len(nums)):
        #     if(nums[p1] == nums[p2]):
        #         return True
        #     else:
        #         p1+=1
        #         p2+=1
        # return False

        #using set 
        # numSet = set(nums)
        # if (len(numSet) == len(nums)):
        #     return False;
        # else:
        #     return True

        #useing hash map
        map = {}
        for  i ,n in enumerate(nums):
            map[i]= n
        num_map = {}
        for n in nums:
            if n in num_map:
                return True
            num_map[n] = 1
        return False
        