#HW 2
#Olivia Guess, Melissa Tully, Sawyer Seitz
#9/20/22

from array import *

class Room():
     def __init__(self, a, b):
        self.vac = a
        self.dirt = b 

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
    rooms = [[Room(False,False) for i in range(ROOM_COLS)] for j in range(ROOM_ROWS)]

    #instance 1
    init_loc = (2,2)
    dirty_squares = [(1,2), (2,4), (3,5)]
    for dirt in dirty_squares:
       rooms[dirt[0]-1][dirt[1]-1].dirt = True
    rooms[init_loc[0]-1][init_loc[1]-1].vac = True
    # for x in range(ROOM_ROWS):
    #     for y in range(ROOM_COLS):
    #         print(rooms[x][y].vac, end='')
    #         print(",", end='') 
    #         print(rooms[x][y].dirt, end=" ")
    #     print()
    # uniform_cost_tree_search(rooms)
    # uniform_cost_graph_search(rooms)
    # iterative_deepening_tree_search(rooms)

     #x = vacuum(0,1), y = dirt(0,1)
    rooms = [[Room(False,False) for i in range(ROOM_COLS)] for j in range(ROOM_ROWS)]

    #instance 2
    for dirt in dirty_squares:
       rooms[dirt[0]-1][dirt[1]-1].dirt = True
    rooms[init_loc[0]-1][init_loc[1]-1].vac = True
    # uniform_cost_tree_search(rooms)
    # uniform_cost_graph_search(rooms)
    # iterative_deepening_tree_search(rooms)

main()