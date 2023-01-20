
import graph
import read_cities
import path

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
            
