a = 61
b = 71
maxim = 0
total = 0
more = 0
maxim2 = 0
for i in range(a, b + 1):
    total = 0
    for j in range(1, b + 1):
        if i % j == 0:
            total += j
        if total >= more:
            more = total
            maxim = i
        if maxim > maxim2:
            maxim2 = maxim
print(maxim2, more)
