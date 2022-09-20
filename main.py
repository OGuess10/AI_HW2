#HW 2
#Olivia Guess, Melissa Tully, Sawyer Seitz
#9/20/22

from array import *

#Rooms
ROOM_TOTAL = 20
ROOM_ROWS = 4
ROOM_COLS = 5

#Action Costs
LEFT = 1.0
RIGHT = 0.9
UP = 0.8
DOWN = 0.7
SUCK = 0.6

def main():

    #x = vacuum(0,1), y = dirt(0,1)
    rooms = [[(0,0) for i in range(ROOM_COLS)] for j in range(ROOM_ROWS)]

    #instance 1
    init_loc = (2,2)
    dirty_squares = [(1,2), (2,4), (3,5)]
    for dirt in dirty_squares:
        rooms[dirt.x][dirt.y].y = 1
    rooms[init_loc.x][init_loc.y].x = 1
    uniform_cost_tree_search(rooms)
    uniform_cost_graph_search(rooms)
    iterative_deepening_tree_search(rooms)

     #x = vacuum(0,1), y = dirt(0,1)
    rooms = [[(0,0) for i in range(ROOM_COLS)] for j in range(ROOM_ROWS)]

    #instance 2
    init_loc = (3,2)
    dirty_squares = [(1,2), (2,1), (2,4), (3,3)]
    for dirt in dirty_squares:
        rooms[dirt.x][dirt.y].y = 1
    rooms[init_loc.x][init_loc.y].x = 1
    uniform_cost_tree_search(rooms)
    uniform_cost_graph_search(rooms)
    iterative_deepening_tree_search(rooms)

main()