class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(0,len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if (    nums[i] + nums[j] == target):
        #             return [i,j]
        # return 
        map = {}
        for i in range(len(nums)):
            targetNums  =  target- nums[i]
            if targetNums  not in map:
                map[nums[i]]= i
            else:
                return [map[targetNums], i]
        # print(map)

        