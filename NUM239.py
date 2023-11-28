t = int(input())

for i in range(t):
    count = 0
    L, R = map(int, input().split())
    for j in range(L, R + 1):
        ldigit = j % 10
        if ldigit == 2 or ldigit == 3 or ldigit == 9:
            count += 1
    print(count)
