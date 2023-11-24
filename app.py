import random
from typing import Literal
from time import sleep
from copy import deepcopy
import sys
from color_utils import black, bright_black, white, bright_white





class Cell:
    value: Literal[0, 1]
    new_born: bool
    just_died: bool

    def __init__(self, value)->None:
        self.value = value
        self.new_born = False
        self.just_died = False
    
    def die(self)->None:
        self.value = 0
        self.just_died = True
        self.new_born = False
    
    def come_alive(self)->None:
        self.value = 1
        self.new_born = True
        self.just_died = False
    
    def steady(self)->None:
        self.new_born = False
        self.just_died = False
    
    def __str__(self)->str:
        if self.new_born:
            return bright_white("#")
        if self.just_died:
            return black("#")
        if self.value == 1:
            return white("#")
        return bright_black("#")

    def __repr__(self)->str:
        return self.__str__()
    
    def __eq__(self, other)->bool:
        return self.value == other.value
    
def dead_state(width: int, height: int) -> list[list[Cell]]:
    return [[Cell(0) for column in range(width)] for row in range(height)]


def dead_or_alive(threshold: float) -> Literal[0, 1]:
    if threshold > 1 or threshold < 0:
        raise ValueError("Aliveness should be in the range 0-1")
    rng = random.uniform(0, 1)
    return 0 if rng >= threshold else 1


def random_state(
    width: int, height: int, threshold: float
) -> list[list[Cell]]:
    if threshold > 1 or threshold < 0:
        raise ValueError("Threshold should be in the range 0-1")
    return [
        [Cell(dead_or_alive(threshold)) for column in range(width)] for row in range(height)
    ]


def render(board: list[list[Cell]]) -> None:
    # Sanity Check
    if not board or not board[0]:
        raise ValueError("Board has no rows")
    if not all([len(board[i]) == len(board[0]) for i in range(len(board))]):
        raise ValueError("Inconsistent Board")

    sys.stdout.write("\x1b[3J")
    sys.stdout.write("\x1b[H")
    render: list[str] = []
    for i, row in enumerate(board):
        row_render = []
        for cell in row:
            row_render.append(str(cell))
        render.append("".join(row_render))
    sys.stdout.write("\n".join(render))


def next_state(board: list[list[Cell]]) -> list[list[Cell]]:
    # Sanity Check
    if not board or not board[0]:
        raise ValueError("Board has no rows")
    if not all([len(board[i]) == len(board[0]) for i in range(len(board))]):
        raise ValueError("Inconsistent Board")

    max_height = len(board)
    max_width = len(board[0])

    new_board = deepcopy(board)

    def get_neighbors(x: int, y: int) -> list[Cell]:
        def filter(p: int, q: int) -> bool:
            return (
                not (p == q == 0)
                and x + p >= 0
                and y + q >= 0
                and x + p < max_height
                and y + q < max_width
            )

        neighbors = [
            board[x + p][y + q] for p in [-1, 0, 1] for q in [-1, 0, 1] if filter(p, q)
        ]
        return neighbors

    for x, row in enumerate(board):
        for y, cell in enumerate(row):
            n_alive = sum([cell.value for cell in get_neighbors(x, y)])
            if not cell.value and n_alive == 3:
                new_board[x][y].come_alive()
            elif cell.value and (n_alive > 3 or n_alive < 2):
                new_board[x][y].die()
            else:
                new_board[x][y].steady()
                

    return new_board


def run(board:list[list[Cell]], speed=0.05):
    while True:
        render(board)
        last_board = board
        board = next_state(board)
        sleep(speed)
        if board == last_board:
            break


def load_from_file(file_path:str)->list[list[Cell]]:
    with open(file_path, 'r') as f:
        lines = f.readlines()
        return [[Cell(int(c)) for c in row if c.isdigit()] for row in lines]


def main():
    print("hi")
    board = None
    if len(sys.argv) > 1:
        try:
            board = load_from_file(sys.argv[1])
        except Exception as e:
            print(f"{sys.argv[1]} is not a valid file\n")
    if not board:
        board = random_state(25, 25, 0.2)
    run(board, 0.1)
if __name__ == "__main__":
    main()