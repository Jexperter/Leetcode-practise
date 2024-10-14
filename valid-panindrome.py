# valid-panindrome (125)
import re

s = "A man, a plan, a canal: Panama"
l = re.sub(r'\W+', '',(s.lower())) # this is with imported module


f = ''.join([char for char in (s.lower()) if char.isalpha()])
print(f)

rev = f[::-1]
print(rev)
print(l)

if f == l:
    print(True)
else:
    print(False)

