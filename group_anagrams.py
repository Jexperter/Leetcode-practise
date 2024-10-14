strs = ["eat","tea","tan","ate","nat","bat"]
res = defaultdict(list)

for s in strs:
    count = [0] * 26 #a ... z

    for c in s:
        count(ord(c) - ord("a")) += 1
    
    


