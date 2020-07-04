# Python program to find all Armstrong numbers in a given range

def is_armstrong(num):
    order = len(str(num))
    total = sum(int(digit) ** order for digit in str(num))
    return num == total

# Example usage
start, end = 1, 500
armstrong_nums = [n for n in range(start, end + 1) if is_armstrong(n)]
print("Armstrong Numbers:", armstrong_nums)