strochka1 = "8" * 70
while "2222" in strochka1 or '8888' in strochka1:
    if "2222" in strochka1:
        strochka1 = strochka1.replace("2222", "88")
    if "8888" in strochka1:
        strochka1 = strochka1.replace("8888", "22")
print("1)",strochka1)

def prost_function(num): #является ли число простым
    for i in range(2,int(num**0.5)+1):
        if (num%i) == 0:
            return False
    return True
for n in range(1000):
    strochka3='>' + 39*'0' + 39*'2' + n*'1'
    while '>1' in strochka3 or '>2' in strochka3 or '>0' in strochka3:
        if '>1' in strochka3:
            strochka3= strochka3.replace('>1','22>')

        if '>2' in strochka3:
            strochka3= strochka3.replace('>2','2>')

        if '>0' in strochka3:
            strochka3 = strochka3.replace('>0','1>')

    sum_ = 0
    for i in strochka3[:-1]:
        sum_ += int(i)
    if prost_function(sum_): #проверка простого числа
        print("3)", n)
        break

strochka4 = '>' + '1' * 11 + '2' * 12 + '3' * 30
while ('>1' in strochka4) or ('>2' in strochka4) or ('>3' in strochka4):
    if '>1' in strochka4:
        strochka4 = strochka4.replace('>1', '22>')
    if '>2' in strochka4:
        strochka4 = strochka4.replace('>2', '2>')
    if '>3' in strochka4:
        strochka4 = strochka4.replace('>3', '1>')
print('4)', strochka4.count('1') + strochka4.count('2') * 2)

for n in range(1, 100):
    strochka2  ="3"*15 + "2"*18 + "1"*n
    while "31" in strochka2 or "33" in strochka2 or "21" in strochka2:
        if "33" in strochka2:
            strochka2 = strochka2.replace("33", "211")
        if "21" in strochka2:
            strochka2 = strochka2.replace("21", "1")
        if "31" in strochka2:
            strochka2 = strochka2.replace("31", "123")
    num = strochka2
    sum_digits = 0
    for digit in num:
        sum_digits += int(digit)
    if sum_digits > 24:
        print("4)", n, strochka2, sum_digits)

        break
