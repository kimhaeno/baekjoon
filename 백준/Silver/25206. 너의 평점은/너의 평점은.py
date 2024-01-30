gsum = 0
sum = 0

for i in range(20):
    name, credit, grade = input().split()

    if grade == "P":
        continue

    c = ord(credit[0]) - ord('0')

    sum += c

    if grade == "F":
        continue

    g = 4 - (ord(grade[0]) - ord('A')) + (0.5 if grade[1] == "+" else 0)
    gsum += g*c

print(gsum/sum)
    
