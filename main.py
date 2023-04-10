counter1 = 0
mx = 0
with open('1_17.txt') as f:
    spisok1 = [int(i) for i in f]
for i in range(len(spisok1)):
    if spisok1[i] % 3 == 0:
        if spisok1[i] % 3 == 0:
            if spisok1[i] % 7 != 0:
                if spisok1[i] % 17 != 0:
                    if spisok1[i] % 19 != 0:
                        if spisok1[i] % 27 != 0:
                            counter1 += 1
                            mx = max(mx, spisok1[i])
print("1)", counter1, mx)

counter2 = 0
counter2_ = 0
mx2 = 0
f2 = open('2_17.txt')
spisok2 = [int(j) for j in f2]
for t in range(len(spisok2)):
    if spisok2[t] % 3 == 0:
        counter2_ += 1
for j in range(len(spisok2)-1):
    if ((spisok2[j] + spisok2[j+1]) < counter2_) and (spisok2[j] < 0 or spisok2[j+1] < 0):
        counter2 += 1
        mx2 = max(mx2, spisok2[j] + spisok2[j+1])
print("2)", counter2, mx2)

counter3 = 0
mx3 = -100001
f3 = open('3_17.txt')
spisok3 = [int(k) for k in f3]
for j in range(len(spisok3)-1):
    if ((spisok3[j] + spisok3[j+1]) >= 100) and (spisok3[j] < 0 or spisok3[j+1] < 0):
        counter3 += 1
        mx3 = max(mx3, spisok3[j] * spisok3[j+1])
print("3)", counter3, mx3)

counter4 = 0
mx4 = 0
f4 = open('4_17.txt')
spisok4 = [int(k) for k in f4]
for j in range(len(spisok4)-1):
    if (spisok4[j] % 117 == min(spisok4)  or spisok4[j+1] % 117 == min(spisok4)):
        counter4 += 1
        mx4 = max(mx4, spisok4[j] + spisok4[j+1])
print("4)", counter4, mx4)

counter5, counter5_, _counter5_ = 0, 0, 0
mx5 = 0
f5 = open('5_17.txt')
spisok5 = [int(k) for k in f5]
for i in range(len(spisok5)):
    if spisok5[i] % 2 != 0:
        counter5_ += spisok5[i]
        _counter5_ += 1
avr = counter5_ // _counter5_
for j in range(len(spisok5)-1):
    if (spisok5[j] < avr and spisok5[j+1] % 5 == 0 ) or (spisok5[j+1] < avr and spisok5[j] % 5 == 0 ):
        counter5 += 1
        mx5 = max(mx5, spisok5[j] + spisok5[j+1])
print("5)", counter5, mx5)


