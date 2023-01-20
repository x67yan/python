
import graph
import read_cities
import path

def tours(g):
    '''
    consumes a Graph g and produces the list of paths which contain every vertex
    in g exactly once. In particular, a path is a list of vertices contained in
    g, such that calling is_path(g,path) produces True.  Note: a Graph with less
    than two nodes cannot have a tour because paths have at least two nodes.
    
    tours: (graphof X Y) -> (listof X)
    
    Example:
    g = Graph()
    for i in range(4):
        g.add_vertex(i)
    for i in range(3):
        g.add_edge(i,i+1,None)
    g.add_edge(3,0,None)
    tours(g) => [[0,1,2,3],[1,2,3,0],[2,3,0,1],[3,0,1,2],
                 [3,2,1,0],[2,1,0,3],[1,0,3,2],[0,3,2,1]]
    '''
    total_paths = []
    minimum_v = 2
    vertices = g.get_vertices()
    if len(vertices) < minimum_v:
        return []
    for vertex in vertices:
        total_paths += paths_v(g, vertex)
    if total_paths == []:
        return []
    return total_paths


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


