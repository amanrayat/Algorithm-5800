# The Algorithm defined below firstly finds the Strongly Connected Components using the Kosaraju Algorithm

# Strongly Connected components
#
#   •	Do DFS from any node in the graph
#   •	Store the vertices in decreasing order of their finish time.
#   •	Now again do the DFS on Transpose of the graph
#   •	The Strongly connected components will be found .

# After finding the SCC, the Longest path from the source Component to any Component in the
# resulting DAG is found using the following Algorithm.
#

# Longest path in DAG
#   •	Length <- 0
#   •	For all source components till graph is null
#   •	Do
#       o	Delete source components
#       o	Length = length +1
#   •	End

# Running time of the Algorithm

#   •	We perform the DFS which takes O (V + E) time
#   •	Transpose of the graph can be taken in Linear time
#   •	We again find the DFS taking O (V + E) time
#   •	Now we find the source component in the graph and delete it and increment the counter
#       o	It takes no more than O (V + E) time.

#   •	Hence the total time taken by the algorithm is  O (V + E) time

# Space Complexity of the Algorithm
# DFS takes the O(V) as the space complexity
# Transposing a graph does not take any auxiliary space

# Hence the total space complexity of the algorithm is O(n)


import sys
from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def newEdge(self, u, v):
        self.graph[u].append(v)

    def DFS_helper(self, v, visited, final, idx):
        visited[v] = True
        final[v + 1] = idx
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFS_helper(i, visited, final, idx)

    def DFS(self, v, visited, idx):
        final = dict()
        self.DFS_helper(v, visited, final, idx)
        return (final)

    # appends the value of the vertices in order of their finish time to the stack , So that we do not
    # sort the vertices, hence saving us O(V log V) time.

    def finishOrder(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.finishOrder(i, visited, stack)
        stack = stack.append(v)

    # creates a graph with reversed edges

    def Transpose(self):
        g = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.newEdge(j, i)
        return g

    def createSCCs(self):
        final_result = dict()
        stack = []
        visited = [False] * (self.V)
        for i in range(self.V):
            if visited[i] == False:
                self.finishOrder(i, visited, stack)
        gt = self.Transpose()
        visited = [False] * (self.V)
        comp_index = 0
        while stack:
            i = stack.pop()
            if visited[i] == False:
                final_result.update(gt.DFS(i, visited, comp_index))
                comp_index = comp_index + 1
        return (final_result)


(num_nodes, edges) = (int(input()), [x.strip().split(" ") for x in sys.stdin.readlines()])
adj = dict()
gt = Graph(num_nodes)

for edge in edges:
    gt.newEdge(int(edge[0]) - 1, int(edge[1]) - 1)
    if int(edge[0]) not in adj:
        adj[int(edge[0])] = []
    if int(edge[1]) not in adj:
        adj[int(edge[1])] = []
    adj[int(edge[0])].append(int(edge[1]))

ssc = gt.createSCCs()

ssc_adj = dict()

for vertex, neighbour_arr in adj.items():
    key = ssc[vertex]
    if key not in ssc_adj:
        ssc_adj[key] = []
    for neighbour in neighbour_arr:
        if ssc[vertex] != ssc[neighbour]:
            ssc_adj[key].append(ssc[neighbour])

            # This function deletes the source node and adds the value one to the count and counts the longest path from the source component to any component

cnt = 0

changing_ssc_adj = ssc_adj.copy()

while len(changing_ssc_adj) > 0:
    cnt = cnt + 1

    ssc_adj_sources = dict()
    for vertex in changing_ssc_adj.keys():
        ssc_adj_sources[vertex] = True

    for vertex, neighbour_arr in changing_ssc_adj.items():
        for neighbour in neighbour_arr:
            ssc_adj_sources[neighbour] = False

    for key, bool_val in ssc_adj_sources.items():
        if bool_val:
            removed = changing_ssc_adj.pop(key)

print(cnt)

