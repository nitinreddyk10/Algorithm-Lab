string = input("Enter the string: ")
n = len(string)


def min_palindrome(string: str):
    n = len(string)
    if n in (0, 1):
        return 0
    if string[0] == string[n-1]:
        return min_palindrome(string[1:n-1])
    else:
        return 1 + min(min_palindrome(string[1:]), min_palindrome(string[:n-1]))

print("Minimum no. of characters to make it a palindrome:", min_palindrome(string))