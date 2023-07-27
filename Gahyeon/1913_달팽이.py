import sys

n = int(sys.stdin.readline())
check = int(sys.stdin.readline())

board = [[0 for _ in range(n)] for _ in range(n)]
x = n // 2
y = n // 2

board[x][y] = 1

# 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

j = 0
cnt = 1
num = 1

while x != 0 or y != 0:
    for _ in range(2):
        for _ in range(cnt):
            num += 1
            nx = x + dx[j]
            ny = y + dy[j]
        
            x, y = nx, ny
            board[x][y] = num
            
            if x == 0 and y == 0:
                break
            
        if x == 0 and y == 0:
            break
        j = (j + 1) % 4
    cnt += 1
        
for b in range(len(board)):
    print(' '.join(str(val) for val in board[b]))
    if check in board[b] :
        re_x = b + 1
        re_y = board[b].index(check) + 1
        
print(re_x, re_y)
