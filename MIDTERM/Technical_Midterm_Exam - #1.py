def is_palindrome(num):
    original_num = num
    reversed_num = 0
    while num > 0:
        remainder = num % 10
        reversed_num = (reversed_num * 10) + remainder
        num //= 10
    return original_num == reversed_num

with open('numbers.txt', 'r') as f:
    for line_number, line in enumerate(f, start=1):
        numbers = [int(x) for x in line.strip().split(',')]
        line_sum = sum(numbers)
        if is_palindrome(line_sum):
            print(f"Line {line_number}: {','.join(map(str, numbers))} (sum {line_sum}) - Palindrome")
        else:
            print(f"Line {line_number}: {','.join(map(str, numbers))} (sum {line_sum}) - Not a palindrome")
