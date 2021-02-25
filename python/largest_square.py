# leetcode problem #1725
from typing import List

def countGoodRectangles(rectangles: List[List[int]]) -> int:
    max_len = []
    counter, max_num = 0, 0

    for [i, j] in rectangles:
        max_len.append(i if i <= j else j)
    for i in max_len:
        if i > max_num:
            max_num = i
            counter = 1
        elif i == max_num:
            counter += 1
    return counter


if __name__ == '__main__':
    
    rectangles = [[2,3],[3,7],[4,3],[3,7]]
    print(countGoodRectangles(rectangles))