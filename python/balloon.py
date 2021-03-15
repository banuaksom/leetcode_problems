# https://leetcode.com/problems/maximum-number-of-balloons/
from typing import List

def maxNumberOfBalloons(text: str) -> int:
        letters = {}
        balloon = {'b': 1, 'a': 1, 'l': 1, 'o': 1, 'n': 1}
        count = 0
        
        for c in text:
            if c in balloon:
                if c in letters:
                    letters[c] += 1
                else:
                    letters[c] = 1
        if (len(letters) < 5 or letters['o'] < 2 or letters['l'] < 2):
            return count

        letters['o'] //= 2
        letters['l'] //= 2

        count = min(letters.values())
        
        return count
        
        
        
       
        
if __name__ == '__main__':
    print(maxNumberOfBalloons('"loonbalxballpoon"'))
    