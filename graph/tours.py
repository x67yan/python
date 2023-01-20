
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
            
