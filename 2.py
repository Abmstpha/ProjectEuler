##By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


def Sumevenfibo(n):
    s=0
    k=0
    if n <= 0:
        return "Invalid input, n should be a positive integer."
    elif n == 1:
        l=[0]
        return l
    elif n == 2:
        l=[0, 1]
        return l
    else:
        l = [0, 1]
        for i in range(2, n):
            l.append(l[-1] + l[-2])
        
    for k in l :
        if k%2==0:
            s+=k
            k+=1
    return s 


def Sumevenfibon(n):
    s = 0
    a, b = 0, 1

    for _ in range(n):
        if b % 2 == 0:
            s += b
        a, b = b, a + b

    return s





    
