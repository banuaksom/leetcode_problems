# leetcode problem #1370 
# https://leetcode.com/problems/increasing-decreasing-string/submissions/
from typing import List


def sortString(s: str) -> str:
    alphabet = [0 for i in range(26)]
    output = ''
    for i in range(len(s)):
        alphabet[ord(s[i]) - ord('a')] += 1 

    found = True

    while(found):
        found = False
        for i in range(26):
            if alphabet[i] > 0:
                found = True
                output += chr(i + 97)
                alphabet[i] -= 1
        
        for j in range(25, -1, -1):
            if alphabet[j] > 0:
                found = True
                output += chr(j + 97)
                alphabet[j] -= 1
        
    return output



    


if __name__ == '__main__':
    sortString("aaaabbbbcccc")
