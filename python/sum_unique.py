# leetcode https://leetcode.com/problems/sum-of-unique-elements/
from typing import List

def sumOfUnique(nums: List[int]) -> int:
    return sum(filter(lambda x: nums.count(x) == 1, nums))

if __name__ == '__main__':
    print(sumOfUnique([1,2,3,2]))