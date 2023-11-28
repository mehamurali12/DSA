rounds = int(input())

cp_1 = 0
cp_2 = 0
mlead = 0
winner = 0

for i in range(rounds):
    p1, p2 = map(int, input().split())
    cp_1 += p1
    cp_2 += p2
    lead = abs(cp_1 - cp_2)

    if lead > mlead:
        mlead = lead
        if cp_1 > cp_2:
            winner = 1
        else:
            winner = 2

print(winner,mlead)