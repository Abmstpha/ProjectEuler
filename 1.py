def belowmult(n):
    s = 0
    i=0
    while i<n:
        if i%3 == 0 or i%5==0:
            s+=i
        i+=1
    return s 
        
    
