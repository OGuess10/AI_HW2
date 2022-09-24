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
   def __init__(self, vac_loc, dirt_loc, cost):
      self.vac_loc = vac_loc
      self.dirt_loc = dirt_loc
      self.children = []
      self.cost = cost
      self.next_actions = ['suck']
      if vac_loc[1] != 1:
         self.next_actions.append('left')
      if vac_loc[1] != 5:
         self.next_actions.append('right')
      if vac_loc[0] != 1:
         self.next_actions.append('up')
      if vac_loc[0] != 4:
         self.next_actions.append('down')

def insert(parent, action):
   child = new_rooms_node(parent, action)
   if child != None:
      parent.children.append(child)
   return child

def new_rooms_node(parent, action):
   if action == 'left':
      cost = 1.0
      new_vac_loc = (parent.vac_loc[0], parent.vac_loc[1] - 1)
   elif action == 'right':
      cost = 0.9
      new_vac_loc = (parent.vac_loc[0], parent.vac_loc[1] + 1)
   elif action == 'up':
      cost = 0.8
      new_vac_loc = (parent.vac_loc[0] - 1, parent.vac_loc[1])
   elif action == 'down':
      cost = 0.7
      new_vac_loc = (parent.vac_loc[0] + 1, parent.vac_loc[1])
   else:
      if parent.vac_loc in parent.dirt_loc:
         parent.dirt_loc.remove(parent.vac_loc)
      cost = 0.6
      new_vac_loc = parent.vac_loc
   return Node(new_vac_loc, parent.dirt_loc, parent.cost + cost)

def uniform_cost_tree_search(tree):
   fringe = [tree.root]
   while(True):
      if len(fringe) == 0:
         return 'FAIL'
      #Find lowest cost node in fringe
      next_node = fringe[0]
      for node in fringe:
         if node.cost < next_node.cost:
            next_node = node
      print(next_node.vac_loc)
      #Check if all rooms are cleaned
      if len(next_node.dirt_loc) == 0:
         return next_node
      #Now expand node
      for action in next_node.next_actions:
         fringe.append(insert(next_node, action))


def main():
   #instance 1
   vacuum = (2,2)
   dirt = [(1,2), (2,4), (3,5)]
   tree = Tree(Node(vacuum,dirt, 0))
   uniform_cost_tree_search(tree)
   # uniform_cost_graph_search(rooms)
   # iterative_deepening_tree_search(rooms)

    #instance 2

main()