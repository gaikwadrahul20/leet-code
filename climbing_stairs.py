def climbStairs(n):
    last = 2
    last_to_last = 1
    for i in range(3,n+1):
        result = last + last_to_last
        last_to_last = last
        last = result
    return result    
print(climbStairs(3))

'''
1  - 1
2 - 2, 11
3 - 111, 12, 21
4 - 1111,  121, 211, 112, 22, - 5
5 - 11111, 1211, 2111, 1121, 221, 1112, 122, 212
'''