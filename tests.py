from app import next_state, Cell
from typing import Literal, Callable
import sys
from color_utils import green, red
def make_board(board:list[list[Literal[0,1]]]) -> list[list[Cell]]:
    return [[Cell(v) for v in row] for row in board]
    

def pass_fail(test:Callable[[], bool])->None:
    name = getattr(test, '__name__', 'Unknown')
    if test():
        sys.stdout.write(f"{name} {green('passed')}!\n")
    else:
        sys.stdout.write(f"{name} {red('failed!')}\n")
        
def test_1()->bool:
    board: list[list[Literal[0,1]]] = [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]]
    
    
    new_board = next_state(make_board(board))
    return new_board == make_board(board)

def test_2()->bool:
    board:list[list[Literal[0,1]]] = [
        [0,0,1],
        [0,1,1],
        [0,0,0]
    ]
    new_board = next_state(make_board(board))
    expected_board:list[list[Literal[0,1]]] = [
        [0,1,1],
        [0,1,1],
        [0,0,0]
    ]
    
    return new_board == make_board(expected_board)

def test_3()->bool:
    board:list[list[Literal[0,1]]] = [
        [0,1,0],
        [1,1,1],
        [0,1,0]
    ]
    new_board = next_state(make_board(board))
    expected_board:list[list[Literal[0,1]]] = [
        [1,1,1],
        [1,0,1],
        [1,1,1]
    ]
    return new_board == make_board(expected_board)


def main():
    pass_fail(test_1)
    pass_fail(test_2)
    pass_fail(test_3)
if __name__ == "__main__":
    main()