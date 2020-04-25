def resolve():
    n, m = map(int, input().split())
    ab = list(map(int, input().split()) for _ in range(m))
    adj = [[False] * n for _ in range(n)]
    for a, b in ab:
        adj[a - 1][b - 1] = True
        adj[b - 1][a - 1] = True
    visited = [False] * n
    visited[0] = True
    print(visited)


def dfs(i, visited):
    visited[i] = True
    ans = 0
    if all(visited):
        visited[i] = False
        return 1



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
        input = """3 3
1 2
1 3
2 3"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """7 7
1 3
2 7
3 4
4 5
4 6
5 6
6 7"""
        output = """1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
    resolve()
