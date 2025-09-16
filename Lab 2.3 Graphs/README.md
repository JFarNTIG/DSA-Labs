# Lab 3 - Graphs

Copyright (C) 2025 Jacob Farnsworth.

* Programmering, datastrukturer och algoritmer

## AI-Deklaration (Lärare)

AI användes ej i framtagandet av denna laboration.

## Setup

### Linux/Windows

```
python -m venv .venv
pip install -r requirements.txt
```

## Introduction

In this lab, you will learn about *graphs* which are a very useful kind of data structure. **Very important to remember**: When we say *graph* in computer science, we are usually referring to the data structure, *not* the kind of graphs you learned about in math class. (We call those kinds of graphs *plots*)

A *graph* consists of a number of *nodes*, and a number of *edges* connecting those nodes.

You can think of graphs this way: A graph is a bit like a binary tree, except instead of nodes having exactly 2 or 0 connections, nodes can have any number of connections (edges) to other nodes.

There are different types of graphs:

* In an *undirected graph*, the edges have no concept of direction. For example, if there is an edge between two nodes A and B, then we say that A and B are 'connected' and this means the same thing as saying that B and A are connected.
* In a *directed graph*, every edge has a direction. For example, if we have two nodes A and B, we could add an edge *from* node A *to* node B. However, there might not be an edge from B to A, so the reverse is not automatically true.


Examples of *undirected graphs*:
* Friendship networks on a social media website. Every node is a profile, and every edge is a friendship relation. Since friendships are mutual (if A is friends with B, then B is automatically friends with A) edges have no direction, thus the graph is undirected.
* Molecules, with atoms as nodes, and chemical bonds as edges.
* Scientific collaboration, with people as nodes, and edges between people if they have authored a paper together.

Examples of *directed graphs*:
* Follow networks on a social media website. Every node is a profile, and an edge from A to B means that A followed B. Follow relationships are not mutual, so edges in this graph always have direction.
* Computer networks, with devices as nodes, and connections as edges.
* Webpage links, with webpages as nodes, and links as edges. This kind of graph is frequently used in web search engines.
* Dependency networks, with tasks as nodes, and dependencies as edges. This kind of graph is frequently used in software build systems to determine which order to build submodules in a large project.


In addition, there are also *weighted graphs*. In a weighted graph, each edge has some associated data, called the weight. Weights usually represent some kind of distance, cost, or time, and can be used to solve optimization problems related to the graph.

Examples of *weighted graphs*:
* Travel networks, where each node is a city or place, and edges represent highways, rail lines or roads between places. The weight assigned to each edge is the distance between the two places. To find the total distance in getting from A to B to C, we can sum up the edge weights along the route.
* Game map graphs, where each node is a location in the map, and edges represent walkable routes from one location to the other. The weight assigned to each edge is the distance between nodes. Games often use such graphs in their AI, so that AI can efficiently pathfind between locations. Enemies might pathfind to the player, to pick up items, or to important locations in the world.


## Assignment

* You **are allowed** to refer to the readings (w3schools, refactoring guru).
* You **are allowed** to use Google to help you understand terms you don't know.
* You **are allowed** to use AI tools to define new terms or get examples.
* You **are not allowed** to use AI tools to complete these tasks (neither writing nor programming) by copy/pasting instructions or code.
* You **are not allowed** to share your solutions with your classmates.

### Understanding Questions.

For each question, remember to **justify your answer**. It's not enough to answer the question, you also have to **explain how you know**.

1. In this lab, we will work with a Python graph library called networkx. We will use graphs to model data about train stations and connections between train stations. Using our graph, we will be able to efficiently compute train routes.

    a. Read example_paths.py. What type of graph is used in this lab? Is it a directed or undirected graph? Is it a weighted graph or unweighted? JUSTIFY YOUR ANSWERS. **How** do you know?

    b. Read example_shortest_path.py. This example uses an algorithm called Dijkstra's algorithm. What is Dijkstra's algorithm used for? Search online and answer: What is the **time complexity** of Dijkstra's algorithm?

    c. Use example_paths.py and example_shortest_path.py and compute both the simple paths and the best path between these stations. Record the output from these examples neatly.
        i. Karlstad C to Jönköping C
        ii. Malmö C to Stockholm C
        iii. Uppsala C to Hallsberg C

    d. Explain in your own words: In a graph, what are *successors* and what are *predecessors*?

    You can read the networkx documentation about successors and predecessors:
    https://networkx.org/documentation/stable/reference/classes/generated/networkx.DiGraph.successors.html
    https://networkx.org/documentation/stable/reference/classes/generated/networkx.DiGraph.predecessors.html

    Finally, run example_graphic.py and look at the plotted graph. Name *two* successors of Uppsala C. 

### YOUR ANSWERS

1.  Write your answers here.

    a. 

    b. 

    c. 

    d. 

### Programming Tasks

Follow the instructions for each task.

1. Start in example_successors.py. Write code that uses networkx to compute and print *all* of the successors of each of these stations. `DiGraph` has a function `successors`, you may call this function for `stations_graph` and print the results.

    Again, I encourage you to read the networkx documentation about successors and predecessors:
    https://networkx.org/documentation/stable/reference/classes/generated/networkx.DiGraph.successors.html
    https://networkx.org/documentation/stable/reference/classes/generated/networkx.DiGraph.predecessors.html

    * Uppsala C
    * Visby

2. Now, we are going to imagine that there are several ongoing rail failures and power outages.
    * Malmö C to Lund C (power outage)
    * Jönköping C to Linköping C (rail failure)
    * Örebro C to Västerås C (rail failure)

    Switch example_paths.py, example_shortest_path.py and example_successors.py to use the rail network with outage data in connections_se_broken.txt. Alternatively, you can update them so they compute paths, shortest paths and successors for *both* the normal network and the outage network at the same time.

    Now, use your code to answer: How do the outages affect passengers traveling from:
    * Malmö C to Växjö C?
    * Karlstad C to Stockholm C?

3. Based on your answer to 2: *At a minimum*, which failures and outages are most urgent to fix for passengers traveling from these cities? MINIMUM means the BARE MINIMUM, as in the LEAST NUMBER of failures that must be fixed. What are the new updated best routes between these cities once the bare minimum of failures are addressed?
    * Malmö C to Växjö C?
    * Karlstad C to Stockholm C?

4. (VG) Searching online, define the following graph terms. For each term, write an example in the examples folder that uses networkx to compute them for our travel graph.
    * Connected components. (add example_components.py)
    * Cycles. (add example_cycles.py)
    * Traveling salesman problem. (add example_salesman.py)
      You can read about the traveling salesman problem here:
      https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.approximation.traveling_salesman.traveling_salesman_problem.html