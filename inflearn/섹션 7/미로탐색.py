def escape_maze(x, y):
    global cnt
    if x == 6 and y == 6:
        cnt += 1
        return
    else:
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x <= 6 and 0 <= next_y <= 6 and maze_map[next_x][next_y] == 0:
                maze_map[next_x][next_y] = 1
                escape_maze(next_x, next_y)
                maze_map[next_x][next_y] = 0

if __name__ == "__main__":
    maze_map = []
    for _ in range(7):
        maze = list(map(int, input().split()))
        maze_map.append(maze)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    cnt = 0
    maze_map[0][0] = 1
    escape_maze(0, 0)
    print(cnt)