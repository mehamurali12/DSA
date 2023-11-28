t = int(input())

for i in range(t):
    n = int(input())
    diff = list(map(int, input().split()))
    count = 0
    for rating in diff:
        if rating >= 1000:
            count += 1
    print(count)
