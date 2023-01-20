import graph
import read_to_graph

def is_path(g, lst):
    '''
    consumes a Graph g and a list of vertices (lst) contained in g, and returns
    True if there is an edge between consecutive vertices in the list, False 
    otherwise.
    
    Requires: 
    Every vertex v in lst is also in g.get_vertices().
    There must be at least two vertices in lst.
    
    is_path: (graphof X Y) (listof X) -> Bool
    
    Examples (using a (graphof Str Y)):
    g = read_cities("cities.txt")
    is_path(g, ["Sao Paolo", "New York", "London"]) => True
    is_path(g, ["Sao Paolo", "New York", "London", "New York"]) => True
    is_path(g, ["Sao Paolo", "New York", "Cairo"]) => False
    '''
    pos = 0
    last_two_pos = len(lst) - 1
    
    while pos < last_two_pos:
        possible_path = g.get_edges(lst[pos])
        if not lst[pos + 1] in possible_path:
            return False
        pos += 1
    return True


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
