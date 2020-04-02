def palindrome(x):

    if x < 0:
        return False
    
    y = str(x)
    lst = list(y)
    lst.reverse()
    w = "".join(lst)
    z = int(w)

    if x == z:
        return True

print(palindrome(-121))