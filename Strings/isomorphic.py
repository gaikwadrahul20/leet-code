def isomor(s,t):
        mapped = [ [None]*2 for i in range(128)]
        i =0
        for i in range(len(s)):
            val = mapped[ord(s[i])][0]
            visited = mapped[ord(t[i])][1]
            if(val is not None and val != t[i]) or (visited is not None and visited != s[i]):
                return False
            # if(visited is not None and visited != s[i]):
            #     return False
            else:
                mapped[ord(s[i])][0] = t[i]
                mapped[ord(t[i])][1] = s[i]
        return True
print(isomor("egg", "add"))
