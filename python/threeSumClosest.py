# https://leetcode.com/problems/3sum-closest/
import math
from typing import List
def threeSumClosest(nums: List[int], target: int) -> int:
    nums.sort()
    min_diff = math.inf
    n = len(nums)

    for i in range(n - 2):
        left, right = i + 1, n - 1

        while left < right:
            target_diff = target - (nums[i] + nums[left] + nums[right])

            if abs(target_diff) < abs(min_diff) or abs(target_diff) == abs(min_diff) and target_diff > min_diff:
                min_diff = target_diff

            if target_diff > 0:
                left += 1
            else:
                right -= 1    

    return target - min_diff

if __name__ == '__main__':
    print(threeSumClosest([-1,2,1,-4], 1))

