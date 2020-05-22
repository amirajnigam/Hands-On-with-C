def setkthbit(j,k):
    return((1 << k) | n)  #it will shift 1 to the left k times of the number and then it will perform or operation

    j = 10
    k = 2

print("Kth bit set number : ", setkthbit(j,k))