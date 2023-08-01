n = int(input())
milk = [ int(input()) for _ in range(n) ]
milk.sort(reverse=True)

shopping = [ m for i, m in enumerate(milk) if i%3 != 2 ]
print(sum(shopping))
