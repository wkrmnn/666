f = open('Задание 11.csv')
k = 0
for i in f:
    d = i.strip().split(';')
    h = [d[0], d[1], d[2], d[3]]
    for j in h:
        if d.count(j) == 4:
            summ = 0
            for g in d:
                if g != j:
                    summ += int(g)
            if summ / 3 < int(j):
                k+=1
                break
print(k)