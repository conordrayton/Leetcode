#check if a number is a palindrome
def isPalindrome(x: int) -> bool:
    return str(x)==str(x)[::-1]


x=isPalindrome(121)
print(x)