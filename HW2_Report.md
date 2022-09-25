# AI 1 Homework 2 Report

Olivia Guess, Melissa Tully <br>

## Implementation
To implement each search algorithm, we created several helper functions and classes. We created a node class that describes each node of a search tree or graph, include parents/children, vacuum location, dirt locations, cost, depth, state, and next possible actions. insert_node and new_rooms_node creates a node from a given parent node and from a specified action. A Tree class was also created to store the root node, which describes the initial environment.

For the uniform cost tree search algorithm, a minimum queue was created for the fringe. Every insertion places that node into sorted order from least to greatest. The initial node is placed into the queue first and is then popped off and expanded. It will expand each possible action of that node and add those nodes to the fringe. This is done repeatedly until the goal state is reached (all rooms are clean), until the time has passed an hour, or there are no more items in the fringe (meaning a solution was not found).

## Programming Language, Hardware
The programming languge we used was Python v3.9. Hardware used was MacBook Pro and ...

## Results

### Instance 1

| Result | Uniform Cost Tree Search| Uniform Cost Graph Search | Iterative Deepening Tree Search |
| --- | --- | --- | --- |
| 1st 5 Exp. Nodes | Start(no action), Suck, Down, Up, Right | --- | --- |
| No. Nodes Expanded | 75494 | --- | --- |
| No. Nodes Generated | 1441976 | --- | --- |
| CPU Execution TIme (seconds) | 4974.9 | --- | --- |
| Solution | Start, Up, Suck, Right, Right, Down, Suck, Down, Right, Suck | --- | --- |
| No. of Moves | 9 | --- | --- |
| Cost of Solution | 6.7 | --- | --- |

### Instance 2

| Result | Uniform Cost Tree Search| Uniform Cost Graph Search | Iterative Deepening Tree Search |
| --- | --- | --- | --- |
| 1st 5 Exp. Nodes | Start, Suck, Down, Up, Right | --- | --- |
| No. Nodes Generated | --- | --- | --- |
| CPU Execution TIme (seconds) | --- | --- | --- |
| Solution | Start, Left, Up, Suck, Up, Right, Right, Down, Down, Suck, Right, Up, Suck | --- | --- |
| No. of Moves | 12 | --- | --- |
| Cost of Solution | 9.3 | --- | --- |

Uniform cost tree search exceeded one hour.
