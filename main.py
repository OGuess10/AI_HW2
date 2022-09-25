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
      if vac_loc[1] > 1:
         self.next_actions.append('left')
      if vac_loc[1] < 5:
         self.next_actions.append('right')
      if vac_loc[0] >1:
         self.next_actions.append('up')
      if vac_loc[0] < 4:
         self.next_actions.append('down')

def insert_node(parent, action):
   child = new_rooms_node(parent, action)
   if child != None:
      parent.children.append(child)
      return child
   return None

class min_queue:
   def __init__(self):
      self.queue = []

   def insert(self, node):
      for i in range(len(self.queue)):
         if node.cost < self.queue[i].cost:
            break
      self.queue.insert(0,node)

   def size(self):
      return len(self.queue)

   def is_empty(self):
      return self.size == 0

   def pop(self):
      return self.queue.pop(0)

def new_rooms_node(parent, action):
   child = Node((0,0),parent.dirt_loc.copy(), 0)
   if action == 'left':
      child.cost = parent.cost + 1.0
      child.vac_loc = (parent.vac_loc[0], parent.vac_loc[1] - 1)
   elif action == 'right':
      child.cost = parent.cost + 0.9
      child.vac_loc = (parent.vac_loc[0], parent.vac_loc[1] + 1)
   elif action == 'up':
      child.cost = parent.cost + 0.8
      child.vac_loc = (parent.vac_loc[0] - 1, parent.vac_loc[1])
   elif action == 'down':
      child.cost = parent.cost + 0.7
      child.vac_loc = (parent.vac_loc[0] + 1, parent.vac_loc[1])
   else: #suck
      if parent.vac_loc in parent.dirt_loc:
         child.dirt_loc.remove(parent.vac_loc)
      child.cost = parent.cost + 0.6
      child.vac_loc = parent.vac_loc
   return child

def uniform_cost_tree_search(tree):
   #fringe = [tree.root]
   fringe = min_queue()
   fringe.insert(tree.root)
   expanded = 0
   while(True):
      if fringe.size == 0:
         return 'FAIL'
      #Pop the lowest cost node in fringe
      next_node = fringe.pop()
      #Check if all rooms are cleaned
      if len(next_node.dirt_loc) == 0:
         print("Vac: ", next_node.vac_loc, "\tCost: ", next_node.cost, "\tDirt: ", next_node.dirt_loc)
         return next_node
      #fringe.remove(next_node)
      #Now expand node
      if expanded < 5:
         print("Vac: ", next_node.vac_loc, "\tCost: ", next_node.cost, "\tDirt: ", next_node.dirt_loc)
         expanded = expanded + 1
      for action in next_node.next_actions:
         fringe.insert(insert_node(next_node, action))


def main():
   #instance 1
   vacuum = (2,2)
   dirt = [(1,2), (2,4), (3,5)]
   tree = Tree(Node(vacuum,dirt, 0.0))
   uniform_cost_tree_search(tree)
   # uniform_cost_graph_search(rooms)
   # iterative_deepening_tree_search(rooms)

    #instance 2

main()