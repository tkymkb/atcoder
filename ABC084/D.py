def resolve():
    q = int(input())
    lr = list(list(map(int, input().split())) for _ in range(q))
    like2017 = []
    leftest = min([l for l, r in lr])
    rightest = max([r for l, r in lr])
    for i in range(leftest, rightest + 1):
        if is_like_2017(i):
            like2017.append(i)

    for l, r in lr:
        c = 0
        for i in range(l, r + 1):
            if i in like2017:
                c += 1
            elif is_like_2017(i):
                like2017.append(i)
                c += 1
        print(c)


def is_like_2017(n):
    is_prime(n) and is_prime((n + 1) // 2)


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True

import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例_1(self):
        input = """1
3 7"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """4
13 13
7 11
7 11
2017 2017"""
        output = """1
0
0
1"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """6
1 53
13 91
37 55
19 51
73 91
13 49"""
        output = """4
4
1
1
1
2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
    resolve()
