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
      self.next_actions = []
      if vac_loc[1] > 1:
         self.next_actions.append('left')
      if vac_loc[1] < 5:
         self.next_actions.append('right')
      if vac_loc[0] > 1:
         self.next_actions.append('up')
      if vac_loc[0] < 4:
         self.next_actions.append('down')
      self.next_actions.append('suck')

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
      j = len(self.queue);
      for i in range(len(self.queue)):
         if node.cost > self.queue[i].cost:
            j = i
            break
      if j == len(self.queue):
         self.queue = self.queue[:j] + [node]
      else:
         self.queue = self.queue[:j] + [node] + self.queue[j:]
      #self.queue.insert(j,node)

   def pop(self):
      return self.queue.pop(len(self.queue)-1)

def new_rooms_node(parent, action):
   #child = Node((0,0),parent.dirt_loc.copy(), 0)
   vac = parent.vac_loc
   cost = parent.cost
   dirts = parent.dirt_loc.copy()
   if action == 'left':
      cost = cost + 1.0
      vac = (parent.vac_loc[0], parent.vac_loc[1] - 1)
   elif action == 'right':
      cost = cost + 0.9
      vac = (parent.vac_loc[0], parent.vac_loc[1] + 1)
   elif action == 'up':
      cost = cost + 0.8
      vac = (parent.vac_loc[0] - 1, parent.vac_loc[1])
   elif action == 'down':
      cost = cost + 0.7
      vac = (parent.vac_loc[0] + 1, parent.vac_loc[1])
   else: #suck
      if parent.vac_loc in parent.dirt_loc:
         dirts.remove(parent.vac_loc)
      cost = cost + 0.6
      vac = parent.vac_loc
   return Node(vac, dirts, cost)

def uniform_cost_tree_search(tree):
   #fringe = [tree.root]
   fringe = min_queue()
   fringe.insert(tree.root)
   expanded = 0
   while(True):
   #for i in range(0,100):
      if len(fringe.queue) == 0:
         print("FAIL")
         return 0
      # print("\n\n")
      # for i in fringe.queue:
      #    print(i.cost, end=" ")
      #Pop the lowest cost node in fringe
      next_node = fringe.pop()

      #Check if all rooms are cleaned
      if len(next_node.dirt_loc) == 0:
         print("Final:")
         print("Vac: ", next_node.vac_loc, "\tCost: ", next_node.cost, "\tDirt: ", next_node.dirt_loc)
         return next_node
      #fringe.remove(next_node)
      #Now expand node
      #if expanded < 5:
      print("Vac: ", next_node.vac_loc, "\tCost: ", next_node.cost, "\tDirt: ", next_node.dirt_loc, "\tActions: ", next_node.next_actions)
      #expanded = expanded + 1
      for action in next_node.next_actions:
         if(next_node.cost < 7.0):
            fringe.insert(insert_node(next_node, action))
            #next_node.next_actions.remove(action)


def main():
   #instance 1
   vacuum = (2,2)
   dirt = [(1,2), (2,4), (3,5)]
   #dirt = [(2,2)]
   tree = Tree(Node(vacuum,dirt, 0.0))
   uniform_cost_tree_search(tree)
   # uniform_cost_graph_search(rooms)
   # iterative_deepening_tree_search(rooms)

    #instance 2

main()