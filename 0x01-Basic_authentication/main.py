#!/usr/bin/env python3
from typing import List
import base64

my_list = [1,3,5,6]

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) //2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    
a = Solution()
result = a.searchInsert(my_list, 7)
print(result)
