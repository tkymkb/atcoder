def resolve():
    n = int(input())
    ab = list(list(map(int, input().split())) for _ in range(n))
    ans = 0
    for a, b in ab[::-1]:
        ans += b - a % b
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
3 5
2 7
9 4"""
        output = """7"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """7
3 1
4 1
5 9
2 6
5 3
5 8
9 7"""
        output = """22"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
    resolve()
