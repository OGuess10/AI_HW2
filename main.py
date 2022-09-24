#HW 2
#Olivia Guess, Melissa Tully
#9/20/22

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

class Tree():
   def __init__(self, root):
      self.root = root

class Node():
   def __init__(self, vac_loc, dirt_loc):
      self.vac_loc = vac_loc
      self.dirt_loc = dirt_loc
      self.children = []

def insert(parent, action):
   child = new_rooms_node(parent, action)
   parent.children.append(child)
   return child

def new_rooms_node(parent, action):
   if action == 'left':
      if parent.vac_loc[1] == 1:
         return None
      else:
         cost = 1.0
         new_vac_loc = (parent.vac_loc[0], parent.vac_loc[1] - 1)
   elif action == 'right':
      if parent.vac_loc[1] == 5:
         return None
      else:
         cost = 0.9
         new_vac_loc = (parent.vac_loc[0], parent.vac_loc[1] + 1)
   elif action == 'up':
      if parent.vac_loc[0] == 1:
         return None
      else:
         cost = 0.8
         new_vac_loc = (parent.vac_loc[0] - 1, parent.vac_loc[1])
   elif action == 'down':
      if parent.vac_loc[0] == 4:
         return None
      else:
         cost = 0.7
         new_vac_loc = (parent.vac_loc[0] + 1, parent.vac_loc[1])
   else:
      if parent.vac_loc in parent.dirt_loc:
         parent.dirt_loc.remove(parent.vac_loc)
      cost = 0.6
      new_vac_loc = parent.vac_loc

   return Node(new_vac_loc, parent.dirt_loc)


def main():

    #x = vacuum(0,1), y = dirt(0,1)
   #  rooms = [[Room(False,False) for i in range(ROOM_COLS)] for j in range(ROOM_ROWS)]

    #instance 1
   vacuum = (2,2)
   dirt = [(1,2), (2,4), (3,5)]
   #  for dirt in dirty_squares:
   #     rooms[dirt[0]-1][dirt[1]-1].dirt = True
   #  rooms[init_loc[0]-1][init_loc[1]-1].vac = True
   tree = Tree(Node(vacuum,dirt))
   uniform_cost_tree_search(tree)
    # uniform_cost_graph_search(rooms)
    # iterative_deepening_tree_search(rooms)

     #x = vacuum(0,1), y = dirt(0,1)
   #  rooms = [[Room(False,False) for i in range(ROOM_COLS)] for j in range(ROOM_ROWS)]

    #instance 2
   #  for dirt in dirty_squares:
   #     rooms[dirt[0]-1][dirt[1]-1].dirt = True
   #  rooms[init_loc[0]-1][init_loc[1]-1].vac = True
    # uniform_cost_tree_search(rooms)
    # uniform_cost_graph_search(rooms)
    # iterative_deepening_tree_search(rooms)

main()