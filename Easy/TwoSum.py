from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers, return indices of the two numbers
        such that they add up to a specific target.
        You may assume that each input would have exactly one solution, and you
        may not use the same element twice.
        Given nums = [2, 7, 11, 15], target = 9,
        Because nums[0] + nums[1] = 2 + 7 = 9,
        return [0, 1].
        :param nums: List[int]
        :param target: int
        :return: List[int]
        """
        seen = dict()

        for index, num in enumerate(nums):
            other = target - num

            if other in seen:
                return [seen[other], index]
            else:
                seen[num] = index

        return []


indices = Solution()
nums = [1, 2, 3, 7]
print(indices.twoSum(nums, 9))
