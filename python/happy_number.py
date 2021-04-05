# Any number will be called a happy number
# if, after repeatedly replacing it with a number
# equal to the sum of the square of all of its digits
# leads us to number ‘1’
# All other (not-happy) numbers will never reach ‘1’

def find_happy_number(num):
    fast, slow = num, num
    while True:
        slow = square_digits(slow)
        fast = square_digits(square_digits(fast))
        if slow == fast:
            break
    return slow == 1

def square_digits(num):
    total = 0
    while (num > 0):
        digit = num % 10
        total += digit * digit
        num //= 10
    return total


if __name__ == '__main__':
    print(find_happy_number(12))
    print(find_happy_number(23))

    