import sys

n = int(sys.stdin.readline())

arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort(reverse=True)

total = 0

for i in range(0, len(arr), 3):
    total += sum(arr[i:3+i][0:2])
    
print(total)