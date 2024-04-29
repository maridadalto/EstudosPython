class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums) -1):
            firstNum = nums[i]

            for j in range( i+1, len(nums)):
                secondNum = nums[j]

                if firstNum == secondNum:
                    return True
        return False