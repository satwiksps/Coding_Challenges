
from math import gcd

def lcm(a, b):
    return (a * b) // gcd(a, b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"GCD: {gcd(a, b)}, LCM: {lcm(a, b)}")
