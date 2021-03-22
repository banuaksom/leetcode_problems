# Given an array of positive numbers and a positive number s,
# find the length of the smallest contiguous subarray
# whose sum is greater than or equal to s
# Return 0 if no such subarray exists

def smallest_subarray_with_given_sum(s, arr):
  ''' O(N) solution'''
  min_len, window_start, num_sum, found = len(arr), 0, 0, 0

  for window_end in range(min_len):
    if arr[window_end] >= s:
      return 1
    num_sum += arr[window_end]
    while num_sum >= s:
      found = 1
      min_len = min(min_len, window_end + 1 - window_start)
      num_sum -= arr[window_start]
      window_start += 1
  
  return min_len if found else 0 

if __name__ == '__main__':
    print(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6]))
  
