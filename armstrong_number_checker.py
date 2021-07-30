
def is_armstrong(number):
    digits = list(map(int, str(number)))
    return sum(d ** len(digits) for d in digits) == number

num = int(input("Enter a number: "))
print("Armstrong number" if is_armstrong(num) else "Not an Armstrong number")
