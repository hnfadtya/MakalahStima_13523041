# Optimization of Fastest Public Transportation Route Selection in Jakarta Metropolitan Area Using Branch and Bound Algorithm

## About
This research addresses the problem of finding the fastest route through public transportation networks in the Jakarta Metropolitan Area (Jabodetabek), which includes various modes such as KRL, MRT, Trans Jakarta, and LRT. The complexity of the transportation system and the absence of an integrated route planning tool often make it difficult for passengers to identify the most efficient path. To solve this, we model the transportation system as a weighted directed graph, where nodes represent stations and edges represent travel segments with associated time costs.

We implement two well-known graph search algorithms—Uniform Cost Search (UCS) and A* Search—to find the shortest travel time between two stations. The A* algorithm utilizes a heuristic function based on mode-switch penalties to improve search efficiency. The system allows users to choose both the algorithm and the start/goal nodes and provides a visualization of the state space tree formed during the search.

## How to Run
cd src
python main.py

## Structure
```
.
├── doc/    # all document-related files
├──src/       
│   ├── algorithm.txt       # UCS and A* algorithm
│   ├── graph_route.txt     # graph as a representation of transportation network
│   ├── visualize.txt       # visualizer
│   └── main.txt            # main program
├── test/                   # test or output file
└── README.md               # here you are
```

## Author
<div align="center">

| NIM      | Nama                      |
|----------|---------------------------|
| 13523041 | Hanif Kalyana Aditya      |

</div>