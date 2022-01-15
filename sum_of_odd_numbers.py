
def sum_of_odds(n):
    return sum(i for i in range(1, n + 1) if i % 2 != 0)

n = int(input("Enter a number: "))
print("Sum of odd numbers:", sum_of_odds(n))
