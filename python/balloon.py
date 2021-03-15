# https://leetcode.com/problems/maximum-number-of-balloons/
from typing import List

def maxNumberOfBalloons(text: str) -> int:
        letters = {}
        balloon = ['b', 'a', 'l', 'l', 'o', 'o', 'n']
        count, precount = 0, 0
        
        for c in text:
            if c in balloon:
                if c in letters:
                    letters[c] += 1
                else:
                    letters[c] = 1
        if len(letters) < 5:
            return 0
        
        while letters:
            precount = 0
            for i in balloon:
                if i in letters.keys():
                    precount += 1
                    letters[i] -= 1
                    if letters[i] == 0:
                        del letters[i]
                if precount == 7:
                    count += 1
       
        return count
if __name__ == '__main__':
    print(maxNumberOfBalloons('"loonbalxballpoon"'))
    