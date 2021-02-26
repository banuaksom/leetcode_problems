# leetcode problem #1370 
# https://leetcode.com/problems/increasing-decreasing-string/submissions/
from typing import List


def sortString(s: str) -> str:
    char_dic = {}   
    output = ''

    for char in s:
        if char in char_dic.keys():
            char_dic[char] += 1
        else:
            char_dic[char] = 1
   

    sorted_keys = sorted(char_dic.keys())
    
    
    while char_dic:
        for i in range(len(sorted_keys)):
            if char_dic[sorted_keys[i]] == 0:
                del char_dic[sorted_keys[i]]
            else:
                output += sorted_keys[i]     
                char_dic[sorted_keys[i]] -= 1
                   
        for i in range(len(sorted_keys) - 1, -1, -1):
            if char_dic[sorted_keys[i]] == 0:
                del char_dic[sorted_keys[i]]
            else:
                output += sorted_keys[i]     
                char_dic[sorted_keys[i]] -= 1
       
    return output


if __name__ == '__main__':
    print(sortString("ddbbdcbccaaa"))