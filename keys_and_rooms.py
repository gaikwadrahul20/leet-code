rooms = [[1],[2],[3],[]]
# rooms = [[1,3],[3,0,1],[2],[0]]
import collections
def canVisitAllRooms(rooms):
        n_rooms = len(rooms)
        visited = [-1 for i in range(n_rooms)]
        queue = collections.deque()
        queue.append(rooms[0])
        visited[0] = 0
        while(queue):
            current = queue.popleft()
            if len(current) !=0:
                for i in current:
                    if visited[i] == -1:
                        visited[i] = 0
                        queue.append(rooms[i])
        if -1 in visited:
            return False
        else:
            return True

print(canVisitAllRooms(rooms))