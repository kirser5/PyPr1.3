import math
def f(n, m):
    a = 0
    b = 0
    c = 0
    for i in range (1, n+1):
        a = a + i**6
        c = c + (math.e**i-i**8-76)
    for j in range (1, m+1):
        b = b + j**7
    return (67*(a+b)-38*c)
n = int(input("Enter n: "))
m = int(input("Enter m: "))
print ('%e' % f(n, m))