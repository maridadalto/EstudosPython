class Solution:
    def containsDuplicate(self, nums : List[int]) -> bool:
        conjunto = set()
        for num in nums:
            if num in conjunto:
                return True
            conjunto.add(num)
        return False