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
    while char_dic:
        for i in range(26):
            if chr(i + 97) in char_dic.keys():
                output += chr(i + 97)
                char_dic[chr(i + 97)] -= 1
                if (char_dic[chr(i + 97)] == 0):
                    del char_dic[chr(i + 97)]
        for i in range(25, -1, -1):
            if chr(i + 97) in char_dic.keys():
                output += chr(i + 97)
                char_dic[chr(i + 97)] -= 1
                if (char_dic[chr(i + 97)] == 0):
                    del char_dic[chr(i + 97)]
       
    return output



    


if __name__ == '__main__':
    sortString("aaabbbcccddd")