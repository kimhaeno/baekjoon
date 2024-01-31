n = int(input())

s = set([])

for i in range(n):
    name, state = input().split()

    if state == "enter":
        s.add(name)
    else:
        s.remove(name)

li = list(s)
li.sort(reverse=True)

for name in li:
    print(name)