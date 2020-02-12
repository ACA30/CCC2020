# When a person has a disease, they infect exactly R other people but only on the very next day. No
# person is infected more than once. We want to determine when a total of more than P people have
# had the disease.

p = int(input()) # total people to be infected
n = int(input()) # day 0
r = int(input()) # value of r
total = n
runs = 0

while total <= p:
    next = n * r
    n = next
    total += next
    runs += 1

print(runs)
    
# n people on day 0 infect r people on day 1
# those people infect r people on day 2