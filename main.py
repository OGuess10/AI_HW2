#HW 2
#Olivia Guess, Melissa Tully
#9/20/22

import time
import datetime
STOP = datetime.datetime.now() + datetime.timedelta(hours=1)
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

#This is a node class for the vacuum world problem
class Node():
   def __init__(self, vac_loc: tuple, dirt_loc: list, cost: float, action: str):
      self.vac_loc = vac_loc
      self.dirt_loc = dirt_loc
      self.children = []
      self.cost = cost
      self.next_actions = []
      self.depth = 0 # used only for Iterative Deeping Search
      self.parent = None # parent node
      #When node is expanded, these are the possible actions/branches it can take
      self.action = action
      if vac_loc[1] > 1:
         self.next_actions.append('left')
      if vac_loc[1] < 5:
         self.next_actions.append('right')
      if vac_loc[0] > 1:
         self.next_actions.append('up')
      if vac_loc[0] < 4:
         self.next_actions.append('down')
      self.next_actions.append('suck')

#This is a tree class with a root node
class Tree():
   def __init__(self, root: Node):
      self.root = root

#this function connects both child and parent nodes and creates a node by calling new_rooms_node function
def insert_node(parent: Node, action: str):
   child = new_rooms_node(parent, action)
   if child != None:
      parent.children.append(child)
      child.parent = parent
      return child
   return None

#This class is a minimum queue, meaning the node with the least cost is at the front of the queue
class min_queue:
   def __init__(self):
      self.queue = []

   def insert(self, node: Node):
      j = len(self.queue)
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

#This function takes a parent node and an action and creates a new node of the action
def new_rooms_node(parent: Node, action: str)-> Node:
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
   elif action == 'suck':
      if parent.vac_loc in parent.dirt_loc:
         dirts.remove(parent.vac_loc)
      cost = cost + 0.6
      vac = parent.vac_loc
   return Node(vac, dirts, cost, action)

#this function takes in a tree with root of the given state, and finds least cost path that will clean all the rooms
def uniform_cost_tree_search(tree: Tree):
   fringe = min_queue()
   fringe.insert(tree.root)
   start = datetime.datetime.now()
   expanded = 0
   generated = 1
   while(True):

      #if running longer than one hour
      if datetime.datetime.now() > STOP:
         print("Time exceeds one hour.")
         print("Nodes Expanded: ", expanded, "\tNodes Generated: ", generated, "\tTime: ", (datetime.datetime.now() - start).total_seconds())
         return 0

      #If solution cannot be found
      if len(fringe.queue) == 0:
         print("FAIL")
         return 0

      #Pop the lowest cost node in fringe
      next_node = fringe.pop()
      expanded = expanded + 1

      #Check if all rooms are cleaned
      if len(next_node.dirt_loc) == 0:
         print("Path was found!")
         print("Nodes Expanded: ", expanded, "\tNodes Generated: ", generated, "\tTime: ", (datetime.datetime.now() - start).total_seconds())
         parent = next_node.parent
         moves = 1
         print("Sequence:")
         while parent != None:
            print(parent.action)
            moves = moves + 1
         print("Number of moves: ", moves)
         print("Cost: ", next_node.cost)
         return next_node

      #Now expand node
      print("First five nodes expanded:")
      if expanded <= 5:
         print(next_node.action)
         #print("Vacuum Position: ", next_node.vac_loc, "\tCost: ", next_node.cost, "\tAction: ", next_node.action, "\tDirt Locations: ", next_node.dirt_loc)
      for action in next_node.next_actions:
        # if((next_node.cost > 5 and len(next_node.dirt_loc) < 3) or next_node.cost <= 5):
         node = insert_node(next_node, action)
         if (node != None):
            fringe.insert(node)
            generated = generated + len(node.next_actions)

def idts_expand(node: Node, fringe: list, first_five: list, num_nodes: int)-> None:
   ''' Expands each possible state after the given node and adds it to the fringe. '''
   new_nodes = []
   for action in node.next_actions:
      new_rooms_node(node, action)

def idts_sol():
   pass

# todo
#  create expand helper function
#  create generate node helper function
#  track time to search
#  create solution list from solution_found
#  print results when solution found
def iterative_deepening_tree_search(tree: Tree):
   ''' BFS, but at increasing depths. '''
   #next node determined by lowest row, then lowest column

   start_time = time.time()
   max_depth = 0 # 0-indexed, root.depth = 0
   solution_node = None
   solution = []
   fringe = []
   first_five= []
   num_nodes_generated = []

   while (True):
      print(f'max depth: {max_depth}')
      num_nodes = 0
      idts_expand(tree.root, fringe, first_five, num_nodes)
      while (True):
         if (len(fringe) == 0): 
            break
         current_node = fringe.pop()
         if (len(current_node.dirt_loc) == 0):
            idts_sol(current_node)
         #expand
         if (current_node.depth >= max_depth):
            break
         idts_expand(current_node, fringe, first_five, num_nodes)
      num_nodes_generated.append((max_depth, num_nodes))
      max_depth = max_depth + 1


   


def main():
   #instance 1
   vacuum = (2,2)
   dirt = [(1,2), (2,4), (3,5)]
   #dirt = [(2,2)]
   tree = Tree(Node(vacuum,dirt, 0.0, None))
   uniform_cost_tree_search(tree)
   # uniform_cost_graph_search(tree)
   # iterative_deepening_tree_search(tree)

   #instance 2

main()