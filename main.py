import heapq
from collections import Counter, namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def  huffman_encode(s):
    h = []
    for symbol, frequency in Counter(s).items():
        h.append((frequency, len(h), Leaf(symbol)))

    heapq.heapify(h)

    count = len(h)
    while len(h) > 1:
        frequency1, _count1, left = heapq.heappop(h)
        frequency2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (frequency1 + frequency2, count, Node(left, right)))
        count += 1

    code = {}
    if h:
        [(_frequency, _count, root)] = h
        root.walk(code,"")
    return code

def main():
    s = input()
    code = huffman_encode(s)
    encoded = "".join(code[symbol] for symbol in s)
    print(len(code), len(encoded))
    for symbol in sorted(code):
        print("{}: {}".format(symbol, code[symbol]))
    print(encoded)

if __name__ == "__main__":
    main()