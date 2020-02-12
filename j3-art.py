# (0,0) is bottom left of canvas

# min function
def min(list):
    smallest = list[0]
    for i in range(len(list)):
        if smallest > list[i]:
            smallest = list[i]
    return smallest

def max(list):
    largest = list[0]
    for i in range(len(list)):
        if largest < list[i]:
            largest = list[i]
    return largest

n = int(input()) # 2 <= n <= 100
coordsx = []
coordsy = []

for x in range(n):
    data = input()
    
    temp = data.split(",")
    
    coordsx.append(int(temp[0]))
    coordsy.append(int(temp[1]))
    
x1 = (min(coordsx) - 1)
y1 = (min(coordsy) - 1)
x2 = (max(coordsx) + 1)
y2 = (max(coordsy) + 1)

print(str(x1) + "," + str(y1))
print(str(x2) + "," + str(y2))