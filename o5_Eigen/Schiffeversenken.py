from random import randint
grid =[["W","W", "W", "W", "W", "W", "W", "W", "S", "W"],
       ["W","W", "W", "W", "W", "W", "W", "W", "S", "W"],
       ["W","S", "W", "W", "W", "W", "W", "W", "S", "W"],
       ["W","S", "W", "W", "W", "W", "W", "W", "S", "W"],
       ["W","S", "W", "S", "S", "S", "S", "W", "S", "W"],
       ["W","W", "W", "W", "W", "W", "W", "W", "W", "W"],
       ["W","W", "W", "W", "W", "W", "W", "W", "W", "W"],
       ["W","W", "S", "W", "W", "W", "S", "S", "W", "W"],
       ["W","W", "S", "W", "W", "W", "W", "W", "W", "W"],
       ["W","W", "W", "W", "W", "W", "W", "W", "W", "W"],]

Schiff_getroffen = "X"
Wasser_getroffen = "0"
Schiff = "S"
Wasser = "W"

def render_grid(l_grid): 
    for row in l_grid :
        for field in row:
            print(field, end="")
        print()
def shoot_on_board(l_grid):
    while True:
        x = randint(0, 9)
        y = randint(0, 9)
        if l_grid [y][x] != Schiff_getroffen and l_grid [y][x]!= Wasser_getroffen:
            return x,y 
def check_end_game(l_grid : list[list[str]]):
    for row in l_grid:
        for field in row:
            if field == Schiff:
                return False
    return True


render_grid(grid)
counter = 0

while not check_end_game(grid):
    x,y = shoot_on_board(grid)
    if grid[y][x] == Schiff:
        grid[y][x] = Schiff_getroffen
    if grid[y][x] == Wasser:
        grid[y][x] = Wasser_getroffen
    counter += 1 
    print("\033[H\033[J", end="")
    render_grid(grid)
    

print(counter)