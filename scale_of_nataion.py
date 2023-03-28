expression_1 = 3*216**4 + 2*36**6 - 648
scale_1 = ""
while expression_1 !=0:
    scale_1 += str(expression_1 % 6)
    expression_1 = expression_1 // 6
scale_1 = scale_1[::-1]
print("1)", scale_1.count('5'))

expression_2 = 4**34 + 5*(4**22) + 4**13 + 2*(4**9) + 82
scale_2 = ""
while expression_2 != 0:
    scale_2 += str(expression_2 % 16)
    expression_2 = expression_2 // 16
scale_2 = scale_2[::-1]
print("2)", "1:", scale_2.count('1'),"",  "2:", scale_2.count('2'),"",  "3:", scale_2.count('3'),"",  "4:", scale_2.count('4'),"", "5:" ,scale_2.count('5'))
print("2)", "6:", scale_2.count('6'),"",  "7:", scale_2.count('7'),"",  "8:", scale_2.count('8'),"",  "9:", scale_2.count('9'),"", "0:", scale_2.count("0"))

expression_3 = (49**6)*(7**19) - 7**9 - 21
scale_3 = ""
while expression_3 !=0:
    scale_3 += str(expression_3 % 7)
    expression_3 = expression_3 // 7
scale_3 = scale_3[::-1]
print("3)", scale_3.count('6'))

for x in '0123456789':
    scale_4 = int('88' + x + '4' + x, 9) + int('7' + x + '344', 9)
    if scale_4 % 67 == 0:
        print("4)", scale_4//67)
        break

for x_ in '0123456789':
    scale_5 = int('28' + x_ + '2', 18) + int('93' + x_ + '5', 12)
    if scale_5 % 133 == 0:
        print("5)", scale_5//133)
        break

spisok_ans = [] #списочек вохможных значений арифм. выражения
for _x_ in '0123456789A':
    for y in '0123456789A':
        scale_6 = int(y + 'AA' + _x_, 12) + int(_x_ + '02' + y, 14)
        if scale_6 % 80 == 0:
            spisok_ans.append(scale_6)
if spisok_ans:
    print("6)", min(spisok_ans) // 80) #находим минимальное значения выражения
