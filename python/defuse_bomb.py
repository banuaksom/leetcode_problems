# https://leetcode.com/problems/defuse-the-bomb/
from typing import List


def decrypt(code: List[int], k: int) -> List[int]:
       
        if k == 0:
            code = [0 for x in code]
            return code
        
        sum_code, cur, end_idx = [], 0, len(code) - 1
        
        for i in code:
            cur += i
            sum_code.append(cur)    
      
        if k > 0:
            for i in range(end_idx + 1):
                if (i + k) <= end_idx:
                    code[i] = sum_code[i + k] - sum_code[i]
                else:
                    idx = k - (end_idx - i) - 1 
                    code[i] = sum_code[end_idx] - sum_code[i] + sum_code[idx] 
        
        elif k < 0:        
            for i in range(end_idx + 1):
                if i < -k:
                    idx = end_idx - (-k - i)
                    if i == 0:
                        code[i] = sum_code[end_idx] - sum_code[idx]
                    else:
                        code[i] = sum_code[i - 1] + (sum_code[end_idx] - sum_code[idx])                       
                elif i == -k:
                    code[i] = sum_code[i - 1]
                else:
                    code[i] = sum_code[i - 1] - sum_code[i - 1 + k]
                    
                    
        return code

if __name__ == '__main__':
    print(decrypt([2,4,9,3,4,5,3,5,6], -4))
    print(decrypt([5,7,1,4], 2))
    print(decrypt([5,7,1,4], 0))
