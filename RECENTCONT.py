t = int(input())

for i in range(t):
    n = int(input())
    ccodes = input().split()
    scount = ccodes.count("START38")
    lcount = n - scount
    print(scount, lcount)
