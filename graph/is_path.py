import check

from a09q1 import Graph 
# uncomment the following if needed
# from a09q1 import equivalent
# from a09q1 import circle_graph
# from a09q1 import k_graph
from a09q2 import read_cities

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

# Tests
g = read_cities("cities.txt")
check.expect("Q3T1", is_path(g, ["Sao Paolo", "New York", "London", "New York", 
                                 "Tokyo"]), True)
check.expect("Q3T2", is_path(g, ["Sao Paolo", "New York", "London", "New York", 
                                 "Las Vegas"]), False)
check.expect("Q3T3", is_path(g, ["Sao Paolo", "Las Vegas"]), False)
check.expect("Q3T4", is_path(g, ["Sao Paolo", "New York", "London", "Tokyo"]),
             False)

        
