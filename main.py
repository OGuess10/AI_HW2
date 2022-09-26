#HW 2
#Olivia Guess, Melissa Tully
#9/20/22

from cgi import print_form
import time
import datetime

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

#Global Stop
STOP = datetime.datetime.now() + datetime.timedelta(hours=1)

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
      self.state = 'open'
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

   def __str__(self) -> str:
      return f'{self.vac_loc}\t{self.dirt_loc}\t{self.depth}\t{self.cost}'

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

   #Insert a node into the queue and place it into sorted order
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

   #pop the least cost node from the queue
   def pop(self):
      return self.queue.pop()

   def pop_graph(self):
      return self.queue.pop(0)

#This function takes a parent node and an action and creates a new node of the action
def new_rooms_node(parent: Node, action: str)-> Node:
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
   child = Node(vac, dirts, cost, action)
   child.parent = parent
   child.depth = parent.depth + 1
   return child

#this function takes in a tree with root of the given state, and finds least cost path that will clean all the rooms
def uniform_cost_tree_search(tree: Tree):
   print("First five nodes expanded:")
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
      if expanded <= 5:
         print(next_node.action)
         #print("Vacuum Position: ", next_node.vac_loc, "\tCost: ", next_node.cost, "\tAction: ", next_node.action, "\tDirt Locations: ", next_node.dirt_loc)
      for action in next_node.next_actions:
        # if((next_node.cost > 5 and len(next_node.dirt_loc) < 3) or next_node.cost <= 5):
         node = insert_node(next_node, action)
         if (node != None):
            fringe.insert(node)
            generated = generated + len(node.next_actions)

#this function expands a node for iterative deepeing tree search
def idts_expand(node: Node, fringe: list)-> int:
   ''' Expands each possible state after the given node and adds it to the fringe. '''
   actions = ['up', 'left', 'suck', 'right', 'down']
   new_nodes = []
   node_action = {}
   for action in node.next_actions:
      node_action[action] = new_rooms_node(node, action)

   # insert new nodes into fringe by lowest coordinates
   for action in actions:
      if action in node_action:
         new_nodes.append((node_action[action], action))
   
   num_nodes_added = len(new_nodes)
   
   while (len(new_nodes) > 0):
      next = new_nodes.pop(0)
      fringe.append(next[0])
      print(f'{next[1]}\t{next[0]}')
   
   return num_nodes_added

#This function prints the solution to the iterative deepening search tree after it has been completed
def idts_sol(goal_node: Node, first_five: list, start_time: float, num_expanded: int, num_generated: int):
   stop_time = time.time()
   exec_time = stop_time - start_time

   solution_path = []
   solution_path.append(goal_node)
   curr_node = goal_node.parent
   while(curr_node.parent != None):
      solution_path.insert(0, curr_node.parent)
      curr_node = curr_node.parent
   
   print('1st Five Expanded Nodes:')
   for i in range(0, 5):
      print(first_five[i])
   print(f'# Expanded: {num_expanded}\t# Generated: {num_generated}\tCPU Time: {exec_time}')
   print('')
   print(f'# Steps: {len(solution_path)}\tCost: {goal_node.cost}')
   for node in solution_path:
      print(node)
   
#This function uses iterative deepening search to find a path to the solution
def iterative_deepening_tree_search(tree: Tree):
   ''' BFS, but at increasing depths. '''

   start_time = time.time()
   max_depth = 0 # 0-indexed, root.depth = 0
   solution_node = None
   fringe = [] # fringe of search
   num_expanded = 0 # total number of expanded nodes
   num_generated = 0 # total number of generated nodes
   first_five= [] # 1st 5 expanded nodes

   while (True):
      print(f' ---------------- Max Depth: {max_depth} ---------------- ')
      fringe.clear()
      fringe.append(tree.root)
      if (len(first_five) < 5):
         first_five.append(tree.root)
      num_generated = num_generated + 1
      
      # BFS at max_depth
      while (True):
         print(f'Fringe Size: {len(fringe)}')
         if (len(fringe) == 0): # stop when fringe empty
            print('Empty Fringe')
            break

         current_node = fringe.pop(0)
         num_expanded = num_expanded + 1
         if (len(first_five) < 5):
            first_five.append(current_node)
         
         print(f'max {max_depth}:\t{current_node}')
         
         if (len(current_node.dirt_loc) == 0): # check goal
            print(' ---- SOLUTION FOUND ---- ')
            idts_sol(current_node, first_five, start_time, num_expanded, num_generated)
            return

         if (time.time() - start_time > 60*60):
            idts_sol(current_node, first_five, start_time, num_expanded, num_generated)
            print('Search time-out')

            return

         if (current_node.depth >= max_depth): # check depth
            continue

         num_generated = num_generated + idts_expand(current_node, fringe)

      max_depth = max_depth + 1

#This function uses a graph to perform a uniform cost search. It finds a path where the cost is the least in order to clean all of the rooms.
def uniform_cost_graph_search(tree: Tree):
   closed = []
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
      if (len(fringe.queue) == 0):
         print("FAIL")
         return 0

      #Pop the lowest cost node in fringe
      next_node = fringe.pop_graph()
      expanded = expanded + 1
      
      #Check if all rooms are cleaned
      if len(next_node.dirt_loc) == 0:
         print("Path was found!")
         print("Nodes Expanded: ", expanded, "\tNodes Generated: ", generated, "\tTime: ", (datetime.datetime.now() - start).total_seconds())
         parent = next_node
         moves = 1
         print("Sequence:")
         sol_sequence = []
         while parent.parent != None:
            sol_sequence.insert(0, parent.action)
            parent = parent.parent
            moves = moves + 1
         print(sol_sequence)
         print("Number of moves: ", moves)
         print("Cost: ", next_node.cost)
         return next_node

      #Check if state of node is open or closed
      if next_node.state != 'closed':
         # Now expand node
         if expanded <= 5:
            print(next_node.action)
         for action in next_node.next_actions:
            node = insert_node(next_node, action)
            # Check if node is in closed
            if (node != None):
               # is_in_closed = False
               # for closed_node in closed:
               #    if ((node.vac_loc[0] == closed_node.vac_loc[0]) and (node.vac_loc[1] == closed_node.vac_loc[1])):
               #       if (len(node.dirt_loc) == len(closed_node.dirt_loc)):
               #          for j in range(0, len(node.dirt_loc)):
               #             if (set(node.dirt_loc[j]) != set(closed_node.dirt_loc[j])):
               #                break 

               #          is_in_closed = True
               # if(not is_in_closed):
               fringe.insert(node)
               generated = generated + len(node.next_actions)
         closed.append(next_node)
         next_node.state = 'closed'


def main():
   #instance 1
   vacuum = (2,2)
   dirt = [(1,2), (2,4), (3,5)]
   tree = Tree(Node(vacuum,dirt, 0.0, None))
   
   STOP = datetime.datetime.now() + datetime.timedelta(hours=1)
   print('Instance 1 Uniform Cost Tree Search')
   # uniform_cost_tree_search(tree)
   
   STOP = datetime.datetime.now() + datetime.timedelta(hours=1)
   print('Instance 1 Uniform Cost Graph Search')
   uniform_cost_graph_search(tree)

   STOP = datetime.datetime.now() + datetime.timedelta(hours=1)
   print('Instance 1 Iterative Deepening Tree Search')
   # iterative_deepening_tree_search(tree)


   ### Instance 2 ###
   vacuum = (3,2)
   dirt = [(1,2), (2,1), (2,4), (3,3)]
   tree = Tree(Node(vacuum,dirt, 0.0, None))

   STOP = datetime.datetime.now() + datetime.timedelta(hours=1)
   print('Instance 2 Uniform Cost Tree Search')
   # uniform_cost_tree_search(tree)
   
   STOP = datetime.datetime.now() + datetime.timedelta(hours=1)
   print('Instance 2 Uniform Cost Graph Search')
   # uniform_cost_graph_search(tree)

   STOP = datetime.datetime.now() + datetime.timedelta(hours=1)
   print('Instance 2 Iterative Deepening Tree Search')
   iterative_deepening_tree_search(tree)

main()