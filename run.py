# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)

print(search.breadth_first_graph_search(ab).path()) # Búsqueda por amplitud/anchura
print(search.depth_first_graph_search(ab).path())   # Búsqueda por profundidad
print(search.breadth_rya_graph_search(ab).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450

#Resultado de ramificación y acotación
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 140 + 80 + 97 + 101 = 418
