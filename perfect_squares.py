import math
def numSquares(n):
    ans = [0]*(n+2)
    perf_sq = []
    # ans[1] = 1
    for i in range(1,n+1):
        if(math.sqrt(i) == math.ceil(math.sqrt(i))):
            ans[i] = 1
            perf_sq.append(i)
        else:
            val = i
            for sq in perf_sq:
                val = min(val,ans[i - sq] + ans [sq])
            ans[i] = val
    return ans[n]



print(numSquares(13))