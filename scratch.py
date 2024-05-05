f = open('../../Library/Application Support/JetBrains/PyCharm2024.1/scratches/БД_ученики..csv')
count_9_250 = 0
count_scores = 0
count = 0
count_49 = 0
count_46 = 0
count_48 =0
while f:
    a = f.readline().split(';')
    if a == ['']:
        break
    if a[2] == '9' and int(a[-1]) > 250:
        count_9_250 += 1
    if a[1] == '3':
        count += 1
        count_scores += int(a[-1])
    if a[1] == '49':
        count_49 += 1
    if a[1] == '46':
        count_46 += 1
    if a[1] == '48':
        count_48 += 1
print('1.', count_9_250)
print('2.' , '{0:.2f}'.format(count_scores/count))
print('3.', '49 школа:', count_49,';','46 школа:', count_46,';','48 школа:', count_48,'.')