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


def paths_v(g,v):
    '''
    returns paths starting from v in g
    
    paths_v: (graph of X Y) -> (listof X)
    '''
    n = len(g.get_vertices())
    paths = []
    possible_path = []
    joint_l = []
    waiting = []
    joint = {}
    waiting.append(v)
    while waiting != []:
        processing = waiting.pop(0)
        visit_check = processing in possible_path
        if not visit_check:
            possible_path.append(processing)
        neighbours = g.get_edges(processing)
        if len(neighbours) == 0 or visit_check:
            if len(possible_path) == n and possible_path not in paths:
                paths.append(possible_path)
            if joint_l != []:
                latest_joint = joint_l[-1]
                waiting = [joint[latest_joint][0]]
                pos = possible_path.index(latest_joint)
                possible_path = possible_path[0: pos + 1]
                joint[latest_joint].pop(0)
                if joint[latest_joint] == []:
                    joint.pop(latest_joint)
                    joint_l.pop(-1)
        elif len(neighbours) > 1:
            joint[processing] = neighbours[1:]
            joint_l.append(processing)
            processing = neighbours[0]
            waiting.append(processing)
        else:
            processing = neighbours[0]
            waiting.append(processing)
    return paths   

