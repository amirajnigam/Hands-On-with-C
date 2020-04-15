def power_of_number(x,n):
    if n == 0:
        return 1
    if n > 0:
        return (x * power_of_number(x, n-1))
    else:
        return 1/ power_of_number(x, -n)
    
print(power_of_number(2,3))
print(power_of_number(2,-3))
