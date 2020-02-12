t = input() # text
s = input() # jumbled string
found = 0

def shift(data, n=0):
    return data[n::] + data[:n:]

for x in range(len(s)):
    newstr = shift(s,x)
    if newstr in t:
        found = 1
        print("yes")
        break
    
if found == 0:
    print("no")