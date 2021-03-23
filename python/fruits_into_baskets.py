# Given an array of characters where each character represents a fruit tree
# you are given two baskets, and your goal is
# to put maximum number of fruits in each basket
# each basket can have only one type of fruit
# return the maximum number of fruits in both baskets

def fruits_into_baskets(fruits):
    types = {}
    window_start = 0
    max_fruits = 0
   
    for window_end in range(len(fruits)):
        if fruits[window_end] in types:
            types[fruits[window_end]] += 1
        else:
            types[fruits[window_end]] = 1
            
        while len(types) > 2:
            left_type = fruits[window_start]
            types[left_type] -= 1
            if types[left_type] == 0:
                del types[left_type]
            window_start += 1
        max_fruits = max(max_fruits, window_end + 1 - window_start)
               
    return max_fruits  

if __name__ == '__main__':
    print(fruits_into_baskets(['A', 'B', 'C', 'A', 'C']))