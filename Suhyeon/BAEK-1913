n = int(input())
where = int(input())
board = [[0 for _ in range(n) ] for _ in range(n)]

idx_x = n//2
idx_y = n//2 
move = [1,n-2, n-1]
move = ['u','r','d','l']
move_x = [-1,0,1,0]
move_y = [0,1,0,-1]

n_move = 1
moved = 1
move_dir = 0

for val in range(1,(n ** 2)+1):
  if moved == 0 :
    move_dir += 1
    if move_dir % 2 == 0:
      n_move += 1
    moved = n_move
    move_dir %= 4
    
  board[idx_x][idx_y] = val

  idx_x += move_x[move_dir]
  idx_y += move_y[move_dir]
  moved -= 1

idx_x = 0
idx_y = 0

for i in range(len(board)):
  for j in range(len(board[i])):
    val = board[i][j]
    if j >= n-1:
      print(val)
    else:
      print(val, end=' ')
    if val == where:
      idx_x = i+1
      idx_y = j+1
print(idx_x, idx_y)
