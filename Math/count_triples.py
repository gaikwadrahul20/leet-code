import math
def countTriples(n):
        count = 0
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                c = math.sqrt(i*i + j*j)
                if(c>n):
                    break 
                if(c/math.trunc(c) == 1.0):
                    count+=1
        return count * 2


print(countTriples(12))
