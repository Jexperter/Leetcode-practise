s = "anagram"
t = "nagaram"

seen = list(s)

for i in t:
    if i in s:
        seen.remove(i)
        print(seen)
        if not seen:
            print('true')
    else:
        print('false')
    
    