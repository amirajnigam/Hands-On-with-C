def pow(x,n):
    if n == 1:
        return x
    if n%2 == 0:
        m = pow(x,n//2)
        return m*m
    else:
        n = pow(x,n//2)
        return n*n*x
    
print(pow(5,5))