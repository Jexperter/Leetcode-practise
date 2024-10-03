s = "aacc"
t = "ccac"

seen = list(s)

for i in t:
    print(i)
    if i in seen:
        seen.remove(i)
        print(seen)

if not seen:
    print('true')
else:
    print('false')
    
    