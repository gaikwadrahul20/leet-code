#  [73, 74, 75, 71, 69, 72, 76, 73]
# [1, 1, 4, 2, 1, 1, 0, 0]

# Solution with stack is remaining
def dailyTemperatures(T):
        size = len(T)
        hash_table = {}
        res = [0] * size
        for i in range(size-1,-1,-1):
            keys = list(hash_table.keys())
            min_index = 30000
            for key in keys:
                if(key>T[i] and hash_table[key] < min_index):
                    min_index = hash_table[key]
                if(min_index != 30000):
                    res[i] = min_index- i                    
            hash_table[T[i]] = i
        return res
print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
