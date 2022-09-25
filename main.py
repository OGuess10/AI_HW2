#HW 2
#Olivia Guess, Melissa Tully
#9/20/22

from cgi import print_form
import time

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

class Node():
   def __init__(self, vac_loc: tuple, dirt_loc: list, cost: float):
      self.vac_loc = vac_loc
      self.dirt_loc = dirt_loc
      self.children = []
      self.cost = cost
      self.next_actions = []
      self.depth = 0 # used only for Iterative Deeping Search
      self.parent = None # parent node
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

class Tree():
   def __init__(self, root: Node):
      self.root = root

def insert_node(parent: Node, action: str):
   child = new_rooms_node(parent, action)
   if child != None:
      parent.children.append(child)
      return child
   return None

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
   else: #suck
      if parent.vac_loc in parent.dirt_loc:
         dirts.remove(parent.vac_loc)
      cost = cost + 0.6
      vac = parent.vac_loc
   child = Node(vac, dirts, cost)
   child.parent = parent
   child.depth = parent.depth + 1
   return child

def uniform_cost_tree_search(tree: Tree):
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

def idts_expand(node: Node, fringe: list, num_nodes: int)-> None:
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
   
   num_nodes + len(new_nodes)
   while (len(new_nodes) > 0):
      next = new_nodes.pop()
      fringe.append(next[0])
      print(f'{next[1]}\t{next[0]}')


def idts_sol(goal_node: Node, first_five: list, start_time: float, num_expanded: int, nodes_gen_depth: list[list]):
   stop_time = time.time()
   exec_time = stop_time - start_time
   
   num_generated = 0
   for pair in nodes_gen_depth:
      num_generated = num_generated + pair[1]

   solution_path = []
   solution_path.append(goal_node)
   curr_node = goal_node.parent
   while(curr_node.parent != None):
      solution_path.insert(0, curr_node.parent)
      curr_node = curr_node.parent
   
   print(' ---- SOLUTION FOUND ---- ')
   print('1st Five Expanded Nodes:')
   for i in range(0, 5):
      print(first_five[i])
   print(f'# Expanded: {num_expanded}\t# Generated: {num_generated}\tCPU Time: {exec_time}')
   print('')
   print(f'# Steps: {len(solution_path)}\tCost: {goal_node.cost}')
   for node in solution_path:
      print(node)
   

# todo
#  track time to search
#  create solution list from solution_found
#  print results when solution found
def iterative_deepening_tree_search(tree: Tree):
   ''' BFS, but at increasing depths. '''

   start_time = time.time()
   max_depth = 0 # 0-indexed, root.depth = 0
   solution_node = None
   fringe = [] # fringe of search
   num_expanded = 0 # total number of expanded nodes
   first_five= [] # 1st 5 expanded nodes
   nodes_gen_depth = [] # Number of nodes generated at each depth

   while (max_depth <= 9):
      print(f' ---------------- Max Depth: {max_depth} ---------------- ')
      num_nodes = 0
      fringe.clear()
      fringe.append(tree.root)
      if (len(first_five) < 5):
         first_five.append(tree.root)
      num_nodes = num_nodes + 1
      
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
            idts_sol(current_node, first_five, start_time, num_expanded, nodes_gen_depth)
            return

         if (current_node.depth > max_depth): # check depth
            continue

         idts_expand(current_node, fringe, num_nodes)

      nodes_gen_depth.append((max_depth, num_nodes))
      # if last two equal, search fails
      if (len(nodes_gen_depth) >= 2 and nodes_gen_depth[-1] == nodes_gen_depth[-2]):
         print('deep search error')
         idts_sol(tree.root, first_five, start_time, num_expanded, nodes_gen_depth)
         return
      max_depth = max_depth + 1
      if (time.time() - start_time > 60*60):
         print('Search time-out')


   


def main():
   #instance 1
   vacuum = (2,2)
   dirt = [(1,2), (2,4), (3,5)]
   tree = Tree(Node(vacuum,dirt, 0.0))
   
   print('Instance 1 Uniform Cost Tree Search')
   # uniform_cost_tree_search(tree)
   
   print('Instance 1 Uniform Cost Graph Search')
   # uniform_cost_graph_search(tree)

   print('Instance 1 Iterative Deepening Tree Search')
   iterative_deepening_tree_search(tree)

   #instance 2
   vacuum = (3,2)
   dirt = [(1,2), (2,1), (2,4), (3,3)]
   tree = Tree(Node(vacuum,dirt, 0.0))

   print('Instance 2 Uniform Cost Tree Search')
   # uniform_cost_tree_search(tree)
   
   print('Instance 2 Uniform Cost Graph Search')
   # uniform_cost_graph_search(tree)

   print('Instance 2 Iterative Deepening Tree Search')
   # iterative_deepening_tree_search(tree)

main()