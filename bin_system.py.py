for n in range(2, 100):
    summ = 0
    s = str(bin(n))[2:]
    for i in range(len(s)):
        summ += int(s[i])
    if summ % 2 != 0:
        s = "10" + s[2:]
        s += "0"
        r = int(s, 2)
    else:
        s = "11" + s[2:]
        s += "1"
        r = int(s, 2)
    if r > 40:
        print(n)
        break