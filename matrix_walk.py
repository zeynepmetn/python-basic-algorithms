def move(grid, direction, position):
    x, y = position

    if direction == 'up' and x > 0 and grid[x - 1][y] == 1:
        x -= 1
    elif direction == 'down' and x < len(grid) - 1 and grid[x + 1][y] == 1:
        x += 1
    elif direction == 'left' and y > 0 and grid[x][y - 1] == 1:
        y -= 1
    elif direction == 'right' and y < len(grid[0]) - 1 and grid[x][y + 1] == 1:
        y += 1

    return x, y


def print_grid(grid, position):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) == position:
                print('X', end=' ')
            elif grid[i][j] == 1:
                print('.', end=' ')
            else:
                print('█', end=' ')
        print()


def main():
    grid = [
        [1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 0, 1, 1],
        [0, 1, 1, 0, 1],
        [1, 1, 1, 1, 3]
    ]
    position = (0, 0)
    print_grid(grid, position)

    while grid[position[0]][position[1]] != 3:
        direction = input("Enter direction (up/down/left/right): ").lower()
        position = move(grid, direction, position)
        print_grid(grid, position)

    print("Congratulations! You reached the destination.")


if __name__ == "__main__":
    main()