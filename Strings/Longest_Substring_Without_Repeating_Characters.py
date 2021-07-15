def lengthOfLongestSubstring(s):
        start = 0
        max_len = 0
        visited = dict()
        for index in range(len(s)):
            if s[index] in visited and start <= visited[s[index]]:
                start = visited[s[index]] + 1
            else:
                max_len = max(max_len, index - start + 1)
            visited[s[index]] = index
        return max_len

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("tmmzuxt"))
print(lengthOfLongestSubstring(""))




