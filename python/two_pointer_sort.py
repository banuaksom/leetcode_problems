# Given an array containing 0s, 1s and 2s
# return sorted array

def two_pointer_sort(arr):
    left, right = 0, len(arr) - 1
    i = 0

    while i <= right:
        if arr[i] == 0:
            arr[left], arr[i] = arr[i], arr[left]
            i += 1
            left += 1
        elif arr[i] == 1:
            i += 1
        else:
            arr[right], arr[i] = arr[i], arr[right]
            right -= 1
    return arr


if __name__ == '__main__':
    print(two_pointer_sort([0,1,2,0,2,2,1,1]))
    print(two_pointer_sort([2,2,1,1,1,0,0,2,0,1]))