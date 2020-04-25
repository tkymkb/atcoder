from collections import deque


def resolve():
    h, w = map(int, input().split())
    maze = list(input() for _ in range(h))
    sy, sx = 0, 0
    gy, gx = h - 1, w - 1
    visited = [[-1 for _ in range(w)] for _ in range(h)]
    shortest = bfs(maze, visited, sy, sx, gy, gx)
    if shortest == -1:
        print(shortest)
    else:
        walls = sum([l.count("#") for l in maze])
        print(h * w - shortest - walls - 1)


def bfs(maze, visited, sy, sx, gy, gx):
    q = deque([[sy, sx]])
    visited[sy][sx] = 0
    while q:
        y, x = q.popleft()
        if y == gy and x == gx:
            return visited[gy][gx]
        for j, k in ([1, 0], [-1, 0], [0, 1], [0, -1]):
            new_y, new_x = y + j, x + k
            if new_y < 0 or new_x < 0 or new_y > gy or new_x > gx:
                continue
            if maze[new_y][new_x] == "." and visited[new_y][new_x] == -1:
                visited[new_y][new_x] = visited[y][x] + 1
                q.append([new_y, new_x])
    return -1


if __name__ == "__main__":
    resolve()
