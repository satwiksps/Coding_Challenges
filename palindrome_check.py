
def is_palindrome(s):
    return s == s[::-1]

string = input("Enter a string: ")
print("Palindrome" if is_palindrome(string) else "Not a palindrome")
