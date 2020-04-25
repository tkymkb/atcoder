def resolve():
    n = int(input())
    p = list(map(int, input().split()))
    now = p[0]
    M, m = -1, -1
    ans = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            M = max(p[i:j])
            p[i:j].remove(M)
            m = max(p[i:j])
            ans += m
            # if p[j] > p[j - 1]:
            #     m = M
            #     M = p[i]
            # ans += m
    print(ans)


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
        input = """3
2 3 1"""
        output = """5"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """5
1 2 3 4 5"""
        output = """30"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """8
8 2 7 3 4 5 6 1"""
        output = """136"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
    resolve()
