# leetcode https://leetcode.com/problems/string-matching-in-an-array/submissions/
from typing import List

def stringMatching(words: List[str]) -> List[str]:
        sort = sorted(words, key=len)
        output = set()
        for i in range(len(sort) - 1):
            for j in range(i + 1, len(sort)):
                if (sort[i] in sort[j]):
                    output.add(sort[i])
        return output


if __name__ == '__main__':
    print(stringMatching(["mass","as","hero","superhero"]))
