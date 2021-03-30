# https://leetcode.com/problems/3sum/
from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
        triplets = []
        n = len(nums)
        nums.sort()
        
        for i in range(n):
            num = nums[i]
            
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
                  
            left, right = i + 1, n - 1
            
            while left < right:
                
                if left == i:
                    left += 1
                if right == i:
                    right -= 1
                    
                cur_sum = nums[left] + nums[right]
                              
                if cur_sum == -num:
                   
                    triplets.append([num, nums[left], nums[right]])
                    
                    left += 1
                    right -= 1
                    
                    while (left < right and nums[left] == nums[left - 1]):
                        left += 1
                    while (left < right and nums[right] == nums[right + 1]):
                        right -= 1           
                
                elif cur_sum > -num:
                    right -= 1
                else:
                    left += 1            
        
        return triplets

if __name__ == '__main__':
    print(threeSum([-1,0,1,2,-1,-4]))