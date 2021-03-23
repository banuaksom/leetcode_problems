# Given a string str
# find the length of the longest substring in it
# with no more than K distinct characters

def longest_substring_with_k_distinct(str, k):
  window_start = 0
  max_length = 0
  letters = {}

  # in the following loop we'll try to extend the range [window_start, window_end]
  for window_end in range(len(str)):  
    if str[window_end] in letters:
      letters[str[window_end]] += 1
    else:
      letters[str[window_end]] = 1 
    
    # shrink the sliding window, until we are left with 'k' distinct characters in the letters
    while len(letters) > k:
      left_char = str[window_start]
      letters[left_char] -= 1
      if letters[left_char] == 0:
        del letters[left_char]
      window_start += 1  # shrink the window
    # remember the maximum length so far
    max_length = max(max_length, window_end - window_start + 1)
  
  return max_length

if __name__ == '__main__':
    print(longest_substring_with_k_distinct('araaci', 2))