x = int(input())
total = 0

for y in range(x):
    if y % 3 == 0:
        total = total + y
    elif y % 5 == 0:
        total = total + y
        
print(total)