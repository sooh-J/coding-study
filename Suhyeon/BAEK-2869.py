a, b, v = map(int, input().split(" "))
day = 0
loc = 0

if a >= v:
  print(1)
else:
  day = 1 + (v - a) / (a - b)
  if (v - a) % (a - b) > 0:
    day += 1
  print(int(day))