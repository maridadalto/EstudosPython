class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):#pega o primeiro numero da lista e percorre
            firstNum = nums[i]

            for j in range(i +1, len(nums)):#pega o segundo numero e realiza a soma
                secondNum = nums[j]
                if firstNum + secondNum == target:
                    return [i,j]
        return[] #retorna vazio caso nao encontre
