def power2(x):
    if((x & (x-1)) == 0):
        return True
    else:
        return False

print( power2(4))