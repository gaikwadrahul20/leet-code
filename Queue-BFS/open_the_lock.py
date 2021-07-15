deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
# ans: 6

# deadends = ["8888"]
# target = "0009"
# # ans: 1
# deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
# target = "8888"
# # ans: -1
# deadends = ["0000"]
# target = "8888"
# ans:-1
import collections
def openLock(deadends, target):
        level = 0
        queue = collections.deque(["0000"])
        visited = [False] * 10000
        deadends = set(deadends)
        while(len(queue) != 0):
            size = len(queue)
            while(size>0):
                current = queue.popleft()
                
                if current in deadends:
                    size-=1
                    continue

                if(current == target):
                    return level

                for i in range(4):
                    if current [i] == '0':
                        val = '9'
                    else:
                        val = str(int(current[i]) - 1)
                    pred = current[0:i] + val + current[i+1:]
                    
                    if current [i] == '9':
                        val = '0'
                    else:
                        val = str(int(current[i]) + 1)
                    succ = current[0:i] + val + current[i+1:]

                    if(visited[int(pred)] is False and pred not in deadends):
                        queue.append(pred)
                        visited[int(pred)] = True

                    if(visited[int(succ)] is False and succ not in deadends):
                        queue.append(succ)
                        visited[int(succ)] = True
                size-=1
                # 0000, 0001, 0009....1000, 9000 (8)
            level+=1
        return -1

print(openLock(deadends,target))


