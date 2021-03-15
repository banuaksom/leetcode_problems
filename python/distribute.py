# leetcode https://leetcode.com/problems/distribute-candies/
from typing import List

def distributeCandies(candyType: List[int]) -> int:
        n = len(candyType) // 2
        c_type = len(set(candyType))
        
        return min(c_type, n)

if __name__ == '__main__':
    print(distributeCandies([1,1,2,2,3,3]))