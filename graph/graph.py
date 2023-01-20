class Graph:
    '''
    A Graph is a (graphof X Y) where X can be Any and Y can be Any
    Fields: 
    '''
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self,v):
        '''
        adds vertex v to the graph and produce nothing (None): once vertex v has
        been added to the graph, the list produced by get_vertices() contains v.
        
        Requires: the graph does not already contain v before calling 
        add_vertex(v), i.e., the list produced by calling get_vertices()
        does not contain v before calling add_vertex(v)
        
        Side Effects: mutates the graph, which contains v immediately after 
        calling add_vertex(v), i.e., the list produced by calling get_vertices()
        contains v immediately after calling add_vertex(v).
        
        add_vertex: (graphof X Y) X -> None
        
        Example:
        g = Graph()
        g.get_vertices() => []
        g.add_vertex(v)
        g.get_vertices() => [v]
        '''
        self.vertices[v] = {}
        
    def get_vertices(self):
        '''
        returns the list of vertices that have been added to the graph using
        the add_vertex function.
        
        get_vertices: (graphof X Y) -> (listof X)
        
        Example: see the add_vertex function.
        '''
        return list(self.vertices.keys())
    
    def add_edge(self, v, neighbour, data):
        '''
        adds an edge from vertex v to the vertex neighbour, and associate data 
        with this edge, and produce nothing (None): once the edge from v to 
        neighbour has been added to the graph, the list of neighbouring vertices
        produced by calling get_edges(v) contains neighbour, and the value 
        produced by calling get_edge_data(v,neighbour) is data.
        
        Requires: the graph does not already contain an edge from v to neighbour
        before calling add_edge(v,neighbour,data), i.e., the list of vertices
        produced by calling get_edges(v) does not contain neighbour before
        calling add_edge(v,neighbour,data).  The graph must also contain v
        and neighbour before calling add_edge(v,neighbour,data).
        
        Side effects: mutates the graph, which contains an edge with associated
        data from vertex v to vertex neighbour immediately after calling 
        add_edge(v,neighbour,data), i.e., the list of vertices produced by 
        get_edges(v) contains neighbour immediately after calling 
        add_edge(v,neighbour,data), and the value produced by calling 
        get_edge_data(v,neighbour) is data.
        
        add_edge: (graphof X Y) X X Y -> None
        
        Example:
        g = Graph()
        g.add_vertex(v)
        g.add_vertex(neighbour)
        g.add_edge(v,neighbour,data)
        g.get_edges(v) => [neighbour]
        g.get_edge_data(v,neighbour) => data
        '''
        self.vertices[v][neighbour] = data
        if not neighbour in self.vertices:
            self.vertices[neighbour] = {}

    def get_edges(self,v):
        '''
        returns the list of vertices neighbouring v that have been added as 
        edges using the add_edge function.
        
        Requires: the graph must contain vertex v, i.e., the list of vertices
        produced by calling get_vertices() must contain v.
        
        get_edges: (graphof X Y) X -> (listof X)
        
        Example: see the add_edge function.
        '''
        return list(self.vertices[v].keys())
    
    def get_edge_data(self,v,neighbour):
        '''
        returns the data associated with the edge from vertex v to vertex 
        neighbour that has been added to the graph using the add_edge function.
        
        Requires: the graph must contain vertices v and neighbour, as well as an
        edge from v to neighbour, i.e., the list of vertices produced by calling
        get_vertices() must contain v and neighbour, and the list of vertices
        neighbouring v produced by calling get_edges(v) must contain neighbour.
        
        get_edge_data: (graphof X Y) X X -> Y
        
        Example: see the add_edge function.
        '''
        return self.vertices[v][neighbour]
  
 
# Helpful functions for testing.
# Strongly consider writing/using different functions instead of changing these.

def equivalent( lst0, lst1 ):
    '''
    return True if lst0 and lst1 contain the same unique elements, False
    otherwise.
    
    Requires: lst0 contains no duplicates, lst1 contains no duplicates.
    
    equivalent: (listof X) (listof X) -> Bool
    '''
    def subset( l0, l1, idx ):
        return idx == len(l0) or (l0[idx] in l1 and subset(l0, l1, idx+1))
    return subset(lst0,lst1,0) and subset(lst1,lst0,0)


def circle_graph(n):
    '''
    return a (graphof Nat Nat) with n vertices linked in a circle by the edges:
        i to i+1 with edge data i,
        i+1 to i with edge data i+1,
        n-1 to 0 with edge data n-1,
        0 to n-1 with edge data n.
        
    circle_graph: Nat -> (graphof Nat Nat)
    '''
    g = Graph()
    for i in range(n):
        g.add_vertex(i)
    if( n == 2 ):
        g.add_edge(0,1,0)
        g.add_edge(1,0,1)
    elif( n > 2 ):    
        for i in range(n):
            g.add_edge(i, (i+1)%n, i)
            g.add_edge((i+1)%n, i, i+1)
    return g
       
       
def k_graph(n):
    '''
    return a circle graph with additional edges between every two unique 
    vertices that were not already linked, so that every vertex has an edge to 
    every other vertex.  These new edges have unique data counting up from n+2.
    
    k_graph: Nat -> (graphof Nat Nat)
    '''
    def adjacent(i,j,n):
        return i == j+1 or i == j-1 or (i == n-1 and j == 0) \
               or (j == n-1 and i == 0)
    g = circle_graph(n)
    c = n+2
    for i in range(n):
        for j in range(n):
            if(i != j and not adjacent(i,j,n)):
                g.add_edge(i,j,c)
                c += 1
    return g

