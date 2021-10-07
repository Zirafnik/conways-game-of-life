import random, time, copy

def game():
    # choose grid height and width
    HEIGHT = int(input('Choose grid HEIGHT: '))
    WIDTH = int(input('Choose grid WIDTH: '))

    new_grid = []

    # fill initial grid
    for i in range(HEIGHT):
        row = []
        
        # fill row with column values
        for j in range(WIDTH):
            if random.randint(0, 1) == 0:
                row.append(' ') # add dead cell
            else:
                row.append('#') # add living cell
        
        new_grid.append(row)

    # main game loop
    while True:
        print()
        print('_' * (WIDTH + 2))

        # print current grid
        current_grid = copy.deepcopy(new_grid)
        for i in range(HEIGHT):
            print('|', end='')
            for j in range(WIDTH):
                print(current_grid[i][j], end='')
            print('|', end='')
            print()

        print('\u203e' * (WIDTH + 2))

        # update new grid
        for i in range(HEIGHT):
            for j in range(WIDTH):
                num_neighbors = 0

                # Get neighboring coordinate values:
                # `% WIDTH & HEIGHT` ensures that coords wrap around the edge if extreme values
                left_coord = (j - 1) % WIDTH
                right_coord = (j + 1) % WIDTH
                top_coord = (i - 1) % HEIGHT
                bottom_coord = (i + 1) % HEIGHT

                if current_grid[top_coord][left_coord] == '#':
                    num_neighbors += 1
                if current_grid[top_coord][j] == '#':
                    num_neighbors += 1
                if current_grid[top_coord][right_coord] == '#':
                    num_neighbors += 1
                if current_grid[i][left_coord] == '#':
                    num_neighbors += 1
                if current_grid[i][right_coord] == '#':
                    num_neighbors += 1
                if current_grid[bottom_coord][left_coord] == '#':
                    num_neighbors += 1
                if current_grid[bottom_coord][j] == '#':
                    num_neighbors += 1
                if current_grid[bottom_coord][right_coord] == '#':
                    num_neighbors += 1

                # check Conway's rules
                if current_grid[i][j] == '#' and (num_neighbors == 2 or num_neighbors == 3):
                    new_grid[i][j] = '#'
                elif current_grid[i][j] == ' ' and num_neighbors == 3:
                    new_grid[i][j] = '#'
                else:
                    new_grid[i][j] = ' '

        time.sleep(0.8)

game()