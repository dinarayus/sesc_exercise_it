import heapq
from collections import Counter, namedtuple

#создаем бинарное дерево
class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0") # асс - ответление
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def  huffman_encode(s):
    h = [] #пустая очередь
    for symbol, frequency in Counter(s).items():  #возвращает пару частота-символ
        h.append((frequency, len(h), Leaf(symbol))) #заполняет очередь

    heapq.heapify(h) #строим очередь

    count = len(h)
    while len(h) > 1: # в очереди есть хотя бы два элемента
        frequency1, _count1, left = heapq.heappop(h) # элемент с минимальной частотой
        frequency2, _count2, right = heapq.heappop(h) # следующий элемент с минимальной частотой
        heapq.heappush(h, (frequency1 + frequency2, count, Node(left, right))) # добавляем в очереь новый элемент
        count += 1

    code = {} #пустой словарь
    if h:
        [(_frequency, _count, root)] = h # root - начальный узел
        root.walk(code,"")  # заполняем словар code
    return code

def main():
    s = input()
    code = huffman_encode(s)
    encoded = "".join(code[symbol] for symbol in s)  # закодированная строка
    print(len(code), len(encoded))
    for symbol in sorted(code):
        print("{}: {}".format(symbol, code[symbol]))
    print(encoded)

if __name__ == "__main__":
    main()