# Social Network Explorer (SNE) - Technical Report

## 1. Design Decisions

- **Profile Storage:** Used a Python Dictionary (Hash Table). This ensures $O(1)$ average time complexity for user lookups and updates.
- **Network Topology:** Implemented an Adjacency List using `defaultdict(set)`. This allows for fast friendship existence checks and is memory-efficient for sparse social graphs.
- **Discovery (BFS):** Chosen for finding the "Shortest Path" (degrees of separation) because BFS explores neighbors layer-by-layer, guaranteeing the minimum distance in an unweighted graph.
- **Exploration (DFS):** Used a recursive DFS with a depth tracker to simulate "Friends-of-Friends" discovery within a specific social circle radius.

## 2. Complexity Analysis

- **Friend Recommendation:** $O(U \cdot I)$ where $U$ is total users and $I$ is average number of interests. We iterate through users and perform set intersections.
- **BFS/DFS:** $O(V + E)$ where $V$ is users and $E$ is friendships.
- **Sorting Recommendations:** $O(K \log K)$ where $K$ is the number of potential suggestions.

## 3. Bonus: Geo DS Choice

For a production-scale geographic friend discovery, I would implement a **Quadtree** or **Geohash**. Unlike a standard list, these spatial data structures allow us to query users within a specific coordinate bounding box in $O(\log n)$ time rather than scanning every user in the database.
