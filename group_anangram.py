def group_anangram(strs):
        hash_table = dict()
        for string in strs:
            key = ''.join(sorted(string))
            if hash_table.get(key) is not None:        
                hash_table[key].append(string)
            else:
                hash_table[key] = []
                hash_table[key].append(string)
        return(list(hash_table.values()))


print(group_anangram(["eat","tea","tan","ate","nat","bat"]))
print(group_anangram([""]))
print(group_anangram(["a"]))