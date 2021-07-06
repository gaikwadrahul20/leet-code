mat = [[0,0,0],[0,1,0],[0,0,0]]
mat = [[0,0,0],[0,1,0],[1,1,1]]
mat = [[1,1,1],[1,1,1],[1,1,0]]

mat = [[0],[0],[0],[0],[0]]

import collections
def updateMatrix(matrix):
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        m = len(matrix)
        n = len(matrix[0])
        result = [[-1 for i in range(n)] for j in range(m)]
        queue = collections.deque()
        for i in range(m):
            for j in range(n):
                if(matrix[i][j] == 0):
                    result[i][j] = 0
                    queue.append((i,j))
        while(queue):
            (l,r) = queue.popleft()
            for i,j in directions:
                dir_i, dir_j = l + i, r + j
                if(dir_i<m and dir_i>=0 and dir_j>=0 and dir_j<n and result[dir_i][dir_j] == -1):
                    result[dir_i][dir_j] = result[l][r] + 1
                    queue.append((dir_i, dir_j))

        return result

print(updateMatrix(mat))

    
