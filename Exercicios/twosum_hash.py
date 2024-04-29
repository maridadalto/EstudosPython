class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_dict = {}
        for i, num in enumerate(nums):
            if target - num in hash_dict:
                return [hash_dict[target-num],i]
            else:
                hash_dict[num] = i
        return[]