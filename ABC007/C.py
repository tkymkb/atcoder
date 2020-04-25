from collections import deque


def resolve():
    r, c = map(int, input().split())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())
    maze = [input() for _ in range(r)]
    sy, sx, gy, gx = sy - 1, sx - 1, gy - 1, gx - 1
    visited = [[-1] * c for _ in range(r)]
    ans = bfs(maze, visited, sy, sx, gy, gx)
    print(ans)


def bfs(maze, visited, sy, sx, gy, gx):
    q = deque([[sy, sx]])
    visited[sy][sx] = 0
    while q:
        y, x = q.popleft()
        if [y, x] == [gy, gx]:
            return visited[y][x]
        for j, k in ([1, 0], [-1, 0], [0, 1], [0, -1]):
            new_y, new_x = y + j, x + k
            if maze[new_y][new_x] == "." and visited[new_y][new_x] == -1:
                visited[new_y][new_x] = visited[y][x] + 1
                q.append([new_y, new_x])

if __name__ == "__main__":
    resolve()
