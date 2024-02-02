# visit = [False for i in range(9)]
answer = []
problem = []

def valid(x, y, n):
    for i in range(9):
        if answer[i][y] == n and i != x:
            return False
        if answer[x][i] == n and i != y:
            return False
    for i in range(9):
        n_x = (x//3)*3 + i//3
        n_y = (y//3)*3 + i%3
        if answer[n_x][n_y] == n and n_x != x and n_y != y:
            return False
    return True

def solve(x, y):

    if x>8 or y>8:
        return True

    next_x = (9*x + y + 1)//9
    next_y = (9*x + y + 1)%9

    if problem[x][y] != 0:
        return solve(next_x, next_y)
    
    for i in range(1, 10):
        if valid(x, y, i):
            answer[x][y] = i
            if solve(next_x, next_y):
                return True
    
    answer[x][y] = 0
    return False

for i in range(9):
    line = list(map(int, input().split()))
    answer.append(line)
    problem.append(line)

if solve(0, 0):
    for i in range(9):
        for j in range(9):
            print(answer[i][j], end=" ")
        print("")




