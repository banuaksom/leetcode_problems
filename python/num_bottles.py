# https://leetcode.com/problems/water-bottles/
from typing import List

def numWaterBottles(numBottles: int, numExchange: int) -> int:
        drink, rest_empty = numBottles, 0
        
        while numBottles > 0:
            empty = numBottles + rest_empty
            numBottles = empty // numExchange
            drink += numBottles
            rest_empty = empty % numExchange if empty >= numExchange else 0
              
        return drink

if __name__ == '__main__':
    print(numWaterBottles(19,4))
    print(numWaterBottles(9,3))
    print(numWaterBottles(5, 5))