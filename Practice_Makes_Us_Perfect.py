problems = []
week = 0
p_values = input().split()

for i in p_values:
    problems.append(int(i))
    
for i in range(4):
    if problems[i] >= 10: 
        week += 1

print(week)

