# AI 1 Homework 2 Report

Olivia Guess, Melissa Tully <br> <br>

## Implementation
To implement each search algorithm, we created several helper functions and classes. We created a node class that describes each node of a search tree or graph, include parents/children, vacuum location, dirt locations, cost, depth, and next possible actions. insert_node and new_rooms_node creates a node from a given parent node and from a specified action. A Tree class was also created to store the root node, which describes the initial environment.

### Overall Program

<p> We created classes for nodes, a minimum queue and trees for our implementation. Each node has many fields indicating its state, including the vacuum and dirt locations, the current cost, possible actions, parent node, depth, and children. The state information for the vacuum and dirty squares are simply kept as ordered pairs as a list type.</p>
<p> The function new_rooms_node is really important to making a new node. It determines the possible actions the vacuum can take from the given state. </p> <br>

### Iterative Deepening Tree Search

<p> This search algorithm has three different functions associated with it - the main function, iterative_deepening_tree_search, and two helper functions, idts_expand and idts_sol. </p><br>
The main function follows the pseudocode closely. It uses various variables to keep track of the necessary statistics. <br>
Idts_expand generates new nodes based on the possible actions of the current state node and adds them to the fringe in smallest coordinate order. <br>
Idts_sol prints out the statics for the search algorithm once the goal is found for a given instance, including the list of nodes on the path to the goal. <br> <br>

### Uniform Cost Tree Search

<p> For the uniform cost tree search algorithm, a minimum queue was created for the fringe. Every insertion places that node into sorted order from least to greatest. The initial node is placed into the queue first and is then popped off and expanded. It will expand each possible action of that node and add those nodes to the fringe. This is done repeatedly until the goal state is reached (all rooms are clean), until the time has passed an hour, or there are no more items in the fringe (meaning a solution was not found). </p>

## Programming Language, Hardware

Language: Python v3.9 <br>
Hardware used was MacBook Pro and a Dell laptop <br>
<p> Both instances of Iterative Deepening Tree Search were run on a Dell laptop with an Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz </p>

## Results

### Instance 1

| Result | Uniform Cost Tree Search| Uniform Cost Graph Search | Iterative Deepening Tree Search |
| --- | --- | --- | --- |
| 1st 5 Exp. Nodes | Start(no action), Suck, Down, Up, Right | --- | Initial state, Up, Left, Right, Down |
| No. Nodes Expanded | 75494 | --- | --- |
| No. Nodes Generated | 1441976 | --- | --- |
| CPU Execution TIme (seconds) | 4974.9 | --- | --- |
| Solution | Start, Up, Suck, Right, Right, Down, Suck, Down, Right, Suck | --- | Start, Up, Suck, Down, Right, Right, Suck, Right, Down, Suck |
| No. of Moves | 9 | --- | 9 |
| Cost of Solution | 6.7 | --- | 6.7 |
### Instance 2

| Result | Uniform Cost Tree Search| Uniform Cost Graph Search | Iterative Deepening Tree Search |
| --- | --- | --- | --- |
| 1st 5 Exp. Nodes | --- | --- | --- |
| No. Nodes Generated | --- | --- | --- |
| CPU Execution TIme (seconds) | --- | --- | --- |
| Solution | --- | --- | --- |
| No. of Moves | --- | --- | --- |
| Cost of Solution | --- | --- | --- |
Uniform cost tree search exceeded one hour.
