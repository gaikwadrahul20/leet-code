class Solution:
    def floodFill(self, image, sr, sc, newColor):
        if(image[sr][sc] == newColor):
            return image
        temp = image[sr][sc]
        image[sr][sc] = newColor
        
        if(sr>0 and image[sr-1][sc] == temp):
            self.floodFill(image, sr-1, sc, newColor)
        if(sr< len(image)-1 and image[sr+1][sc] == temp):
            self.floodFill(image, sr+1, sc, newColor)
        if(sc >0 and image[sr][sc-1] == temp):
            self.floodFill(image, sr, sc-1, newColor)
        if(sc < len(image[0])-1 and image[sr][sc+1] == temp):
            self.floodFill(image, sr, sc+1, newColor)
        return image
#NOte: do this problem using DFS and stack (not system stack)