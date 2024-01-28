import sys
stack = [0 for i in range(1000000)]
slen = 0

n = int(input())

for i in range(n):
    cmd = sys.stdin.readline().strip()

    if cmd[0] == '1':
        stack[slen] = int(cmd.split()[1])
        slen+=1
    elif cmd[0] == '2':
        if slen != 0:
            print(stack[slen-1])
            slen-=1
        else:
            print(-1)
    elif cmd[0] == '3':
        print(slen)
    elif cmd[0] == '4':
        print(1 if slen == 0 else 0)
    elif cmd[0] == '5':
        print(stack[slen-1] if slen != 0 else -1)
    
    