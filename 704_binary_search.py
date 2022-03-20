#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List


class Solution:
    def search_1(self, nums: List[int], target: int) -> int:
        # 左闭右闭区间
        left, right = 0, len(nums) - 1
        
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle

        return -1
    
    def search(self, nums: List[int], target: int) -> int:
        # 左闭右开区间
        left, right = 0, len(nums)

        while left < right:
            middle = (left + right) // 2
            if nums[middle] > target:
                right = middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        
        return -1


if __name__ == '__main__':
    solution = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    result_index = solution.search(nums, target)
    print(result_index)