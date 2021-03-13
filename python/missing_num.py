# leetcode https://leetcode.com/problems/missing-number/
from typing import List
def missingNumber(nums: List[int]) -> int:
        sum_idx = 0
        
        for i in range(len(nums) + 1):
            sum_idx += i      
        
        return (sum_idx - sum(nums))

if __name__ == '__main__':
    print(missingNumber([9,6,4,2,3,5,7,0,1]))