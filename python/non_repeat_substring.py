# Given a string s, 
# find the length of the longest substring
# which has no repeating characters

def non_repeat_substring(s):
  start, last_occur, longest = 0, {}, 0
  
  for end in range(len(s)):
    char = s[end]

    if char in last_occur:
      start = max(start, last_occur[char] + 1)
    
    last_occur[char] = end
    longest = max(longest, end + 1 - start)

  return longest

if __name__ == '__main__':
    print(non_repeat_substring('arabcbfgggggsjsjksjaci'))