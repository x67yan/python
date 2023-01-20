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
