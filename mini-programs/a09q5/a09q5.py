
import check

from a09q1 import Graph
# uncomment the following if needed
from a09q1 import equivalent
# from a09q1 import circle_graph
# from a09q1 import k_graph
from a09q2 import read_cities
# from a09q3 import is_path
from a09q4 import tours

def path_length(cities, path):
    '''
    consumes a Graph (cities) and a (listof Str) path and returns the sum of 
    the distances (stored as edge data in cities) between consecutive 
    cities/vertices in path.
    
    Requires: 
    Every vertex v in path is also in cities.get_vertices().
    There must be at least two vertices in path.
    is_path(cities,path) must produce True.
    
    path_length: (graphof Str Nat) (listof Str) -> Nat
    
    Example:
    g = Graph()
    g.add_vertex("a")
    g.add_vertex("b")
    g.add_vertex("c")
    g.add_edge("a","b", 1)
    g.add_edge("b","c", 2)
    path_length(g, ["a","b","c"]) => 3
    '''
    length = 0
    edges = len(path) - 1
    pos_vertex = 0
    pos_neighbour = 1
    for i in range(edges):
        length += cities.get_edge_data(path[pos_vertex], path[pos_neighbour])
        pos_vertex += 1
        pos_neighbour += 1
    return length

# Tests
g = read_cities("cities1.txt")
check.expect("Q5T1", path_length(g, ["New York", "London"]), 450)
check.expect("Q5T2", path_length(g, ["New York", "London", "New York"]), 850)
check.expect("Q5T3", path_length(g, ["New York", "London", "Paris"]), 550)


def shortest_tour(cities):
    '''
    consumes a Graph (cities) and returns the tour of cities with the shortest
    path length.  If there is no such tour, return []; if there are multiple
    shortest tours, arbitrarily return one of the shortest tours.  See 
    documentation of tours() for a definition of "tour" and "path".  
    
    shortest_tour: (graphof Str Nat) -> (listof Str)
    
    Example:
    g = Graph()
    g.add_vertex("a")
    g.add_vertex("b")
    g.add_vertex("c")
    g.add_edge("a","b", 1)
    g.add_edge("b","c", 2)
    g.add_edge("c","a", 3)
    g.add_edge("b","a", 4)
    g.add_edge("c","b", 5)
    g.add_edge("a","c", 6)
    shortest_tour(g) => ["a","b","c"]
    '''
    empty = []
    unique = 1
    lst = tours(cities)
    if lst == empty:
        return empty
    path = lst[0]
    if len(lst) == unique:
        return path
    length = path_length(cities, path)
    for new_path in lst[1:]:
        l_path = path_length(cities, new_path)
        if l_path < length:
            path = new_path
            length = l_path
    return path

# Tests
g = read_cities("cities1.txt")
check.expect("multi_path", equivalent(shortest_tour(g),
                                      ["Cairo", "Sao Paolo", "New York", 
                                       "London", "Paris", "Tokyo"]), True)

g = read_cities("empty.txt")
check.expect("no_path", shortest_tour(g), [])

g = read_cities("two_cities1.txt")
check.expect("one_path", shortest_tour(g), ["London", "New York"])

g = read_cities("multi_same_path.txt")
check.expect("multi_same_path", equivalent(shortest_tour(g), ["L", "M", "N"]),
             True)
