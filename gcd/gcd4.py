# Scab Backward with no list

def gcd(m,n):
    
    i = min(m,n)

    while i > 0:
        if(m%i) == 0 and (n%i) == 0:
            return(i)
        i = i-1
print(gcd(14,63))