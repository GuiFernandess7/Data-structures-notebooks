from itertools import combinations

class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = set()
        if len(nums) > 4:
            nums = list(dict.fromkeys(nums))

        for combination_pair in self.get_combinations(nums):
            if sum(combination_pair) == target:
                result = set(
                    index for index, value in enumerate(nums)
                    if value in combination_pair
                )
        return list(result)

    def get_combinations(self, nums):
        """
        :type nums: List[int]
        """
        if len(nums) < 1:
            raise ValueError('Nums length needs to be greater than 2')

        comb = combinations(nums, 2)
        return comb

if __name__=="__main__":
    s = Solution()
    nums = [5, 3, 5, 3]
    solution = s.twoSum(nums, 8)
    print(solution)