# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, anm/
expression_1 = 125**4 + 25**8 - 30
scale_1 = ""
while expression_1 !=0:
    scale_1 += str(expression_1 % 5)
    expression_1 = expression_1 // 5
scale_1 = scale_1[::-1]
print("10)", scale_1.count('4'))

counter13, counter13_, _counter13_ = 0, 0, 0
mx13 = 0
f13 = open('v2_13.txt')
spisok13 = [int(k) for k in f13]
for i in range(len(spisok13)):
    if spisok13[i] % 2 != 0:
        counter13_ += spisok13[i]
        _counter13_ += 1
avr = counter13_ // _counter13_
for j in range(len(spisok13)-1):
    if (spisok13[j] < avr and spisok13[j+1] % 5 == 0 ) or (spisok13[j+1] < avr and spisok13[j] % 5 == 0 ):
        counter13 += 1
        mx13 = max(mx13, spisok13[j] + spisok13[j+1])
print("13)", counter13, mx13)

#ex14
counter14 = 0
f14 = open('v2_14.txt')
for s14 in f14:
    stroka14 = list(map(int, s14.split()))
    if stroka14[0] + stroka14[1] == stroka14[2] + stroka14[3]:
        m = 1
    else:
        m = 0
    if stroka14[3] + stroka14[0] == stroka14[2] + stroka14[1]:
        n = 1
    else:
        n = 0

    if stroka14[3] + stroka14[1] == stroka14[2] + stroka14[0]:
        k = 1
    else:
        k = 0
    minmax1 = sum(stroka14)-2*max(stroka14) - min(stroka14)
    ost1 = max(stroka14) - min(stroka14)
    if (minmax1 > ost1 and m == 1) or (minmax1 > ost1 and n == 1) or (minmax1 > ost1 and k == 1):
        counter14 += 1
print("14)", counter14)

#ex4
for A in range(1,1001):
    F=True
    for x in range(1,73):
        if (((72 % x == 0)<=(90 % x != 0)) or (A-x > 80))==0 :
            F= False
    if F:
        print("4)", A)
        break

for A3 in range(0,1000):
    F3=True
    for x3 in range(0,100):
        for y3 in range(0, 100):
            if ((2 * x3 + 3 * y3 < 30) or (x3 + y3 >= A3))==0:
                F3= False
    if F3:
        print("3)",A3)#долго выводить будет

    spisok_ans = []  # списочек вохможных значений арифм. выражения
    for _x_ in '01234567':
        for y_ in '01234567':
            scale_ = int(_x_ + '01' + y_ + "4", 9) + int(_x_ + y_ + '544', 8)
            if scale_ % 89 == 0:
                spisok_ans.append(scale_)
    if spisok_ans:
        print("11)", min(spisok_ans) // 89)  # находим минимальное значения выражения
        break
strochka = "1" * 101 + "9"*100
while "19" in strochka or '299' in strochka or '3999' in strochka:
    strochka = strochka.replace("19", "2", 1)
    strochka = strochka.replace("299", "3", 1)
    strochka = strochka.replace("3999", "1", 1)
print("12)",strochka)