#ex2
counter = 0
f = open('9_2.txt')
for s in f:
    stroka = list(map(int, s.split()))
    ost = sum(stroka) - max(stroka)-min(stroka)
    minmax = max(stroka) + min(stroka)
    if minmax < ost:
        counter += 1
print("2)", counter)
#ex5
counter5 = 0
f5 = open('9_5.txt')
for s5 in f5:
    stroka5 = list(map(int, s5.split()))
    if stroka5[0] + stroka5[1] == stroka5[2] + stroka5[3]:
        m = 1
    else:
        m = 0
    if stroka5[3] + stroka5[0] == stroka5[2] + stroka5[1]:
        n = 1
    else:
        n = 0

    if stroka5[3] + stroka5[1] == stroka5[2] + stroka5[0]:
        k = 1
    else:
        k = 0
    minmax1 = sum(stroka5)-2*max(stroka5) - min(stroka5)
    ost1 = max(stroka5) - min(stroka5)
    if (minmax1 > ost1 and m == 1) or (minmax1 > ost1 and n == 1) or (minmax1 > ost1 and k == 1):
        counter5 += 1
print("5)", counter5)
