def myPow(x,n):
    if n<0:
        x = 1.0/x
        n = abs(n)
    if n ==1:
        return x
    if n==0:
        return 1.0
    if n % 2==0:
        return myPow(x*x,n/2)
    else:
        return x*myPow(x*x,(n-1)/2)

print(myPow(1.00012,1024))
