# Given an array arr of unsorted numbers and a target sum
# count all triplets in it such that arr[i] + arr[j] + arr[k] < target
# where i, j, and k are three different indices
# return the count of such triplets


def triplet_with_smaller_sum(arr, target):
    arr.sort()
    count = 0
    n = len(arr)
    print(arr)

    for i in range(n - 2):
        left, right = i + 1, n - 1

        while left < right:
            cur_sum = arr[i] + arr[left] + arr[right]
            if cur_sum < target:    
                count += right - left              
                left += 1       
            else:
                right -= 1
        
        return count

if __name__ == '__main__':
    print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))
    print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))