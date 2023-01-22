# Given an integer x, return true if x is a palindrome, and false otherwise.

def isPalindrome(x: int) -> bool:
    x = str(x)
    temp = []
    for i in range(len(x)-1, -1, -1):
        temp.append(x[i])
    temp = ''.join(temp)
    if temp == x:
        return True
    else:
        return False

        