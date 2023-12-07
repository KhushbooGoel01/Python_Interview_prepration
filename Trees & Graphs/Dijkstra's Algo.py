

import heapq

def dijkstra(g, s):

    d = {node: float('infinity') for node in g}
    d[s]=0
    heap =[(0,s)]
   
    while heap:
        l,n = heapq.heappop(heap)
        if  d[n] < l: continue
        for nn,dd in g[n]:
            if l+dd<d[nn]:
                d[nn] = l+dd
                heapq.heappush(heap,( l+dd, nn))

    return d


   
  
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1 ),('C', 2),('D', 5)],
    'C': [('A', 4 ),('B', 2 ),('D', 1)],
    'D': [('B', 5 ),( 'C', 1)]
}



source_vertex = 'A'
result = dijkstra(graph, source_vertex)

# Output the result
print(f"Shortest distances from {source_vertex}: {result}")
