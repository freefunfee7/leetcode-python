#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 双指针法：快、慢指针
        slow = fast = 0
        
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        
        return slow