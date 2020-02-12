# (0,0) is bottom left of canvas
# this is probably the worst and most complicated solution ever im sorry its so sus
# i forgot how to splice strings that would have made this 100x easier...

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
    limit = len(data)
    
    if limit == 3:
        x = data[0]
        y = data[2]
    elif limit == 4:
        x = data[0]
        if data[1] != ",":
            x += data[1]
            y = data[3]
        else:
            y = data[2]
            y += data[3]
    elif limit == 5:
        x = data[0]
        if data[1] != ",":
            x += data[1]
            if data[2] != ",":
                x += data[2]
            else:
                y = data[3]
                y += data[4]
        else:
            y = data[2]
            y += data[3]
            y += data[4]
    elif limit == 6:
        x = data[0]
        x += data[1]
        if data[2] != ",":
            x += data[2]
            y = data[4]
            y += data[5]
        else:
            y = data[3]
            y += data[4]
            y += data[5]
            
    elif limit == 7:
        x = data[0]
        x += data[1]
        x += data[2]
        y = data[4]
        y += data[5]
        y += data[6]
    
    # x = data[0]
    # x += data[1]
    # y = data[3]
    # y += data[4]
    
    coordsx.append(int(x))
    coordsy.append(int(y))
    
x1 = (min(coordsx) - 1)
y1 = (min(coordsy) - 1)
x2 = (max(coordsx) + 1)
y2 = (max(coordsy) + 1)

print(str(x1) + "," + str(y1))
print(str(x2) + "," + str(y2))