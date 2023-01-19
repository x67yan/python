##
## **********************************************
##   Xueyao Yan (20775321)
##   CS116  Spring 2019
##   Assignment 09,  Bonus
## **********************************************
##
import check

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
   

def read_cities(filename):
    '''
    returns a (graphof Str Nat) containing the cities listed in the file 
    described by the filename string.
    
    Requires: filename is the name of an existing file whose contents are 
    formatted as follows.  
    
    The first line contains the number M of cities that need to be stored in the 
    graph.  This natural number M must be greater than or equal to 0.  
    
    Each of the next M lines contain the unique name of a city, e.g., 
    "Waterloo", "Waterloo, ON", "Terre Haute, IN, USA", "South Park" and 
    "Imaginationland".
    
    The next line contains the number N of edges that need to be stored in the 
    graph.  This natural number N must be greater than or equal to 0.  
    
    Each edge is stored across three lines (so there are 3N edge lines in 
    total).  An edge "leaves" a source city/vertex and "arrives" at a neighbour
    city/vertex.  The data associated with the edge is the distance between the
    two cities.
    
    The first line of an edge is the name of the source vertex, which is one of
    the M listed cities.  The second line of an edge is the name of the 
    neighbour vertex, which is one of the *other* M listed cities (it cannot be
    the same as the source).  The third line of an edge contains a natural 
    number D greater than zero, and it is the (unitless) distance between the 
    two cities, e.g., 500.
    
    read_cities: Str -> (graphof Str Nat)
    
    Example:
    The contents of the file with filename "cities.txt" is below, followed by 
    the Graph that corresponds to that file.  Note that the comments on the
    right are not actually in that file, they are only shown here for 
    illustration.
    
    Note that the edges don't always go both ways: New York is connected to 
    Tokyo, but Tokyo is not connected to New York.  Also note that when the 
    edges go both ways, the distance might not be equal (e.g., due to one way 
    roads, different flight paths, etc): London to New York is 400, but New York
    to London is 450.  Also note that some cities may not have any edges leaving
    (Cairo, Las Vegas), and some cities may not have any edges arriving (Sao 
    Paolo, Las Vegas); Las Vegas is an example of a city that has no edges 
    leaving or arriving.  The distances are not guaranteed to be unique.
        
    7           <--- Number of cities (1 line)
    London      <--\
    Paris          |
    Tokyo          |
    New York       | 7 cities (7 lines)
    Las Vegas      |
    Sao Paolo      |
    Cairo       <--/
    8           <--- Number of edges (1 line)
    London      <-------------------------\
    Paris                                 |
    100                                   |
    London                                |
    New York                              |
    400                                   |
    Paris       <--\ Edge leaving Paris,  |
    London         | arriving London,     |
    100         <--/ distance=100         |
    New York                              |
    London                                |
    450                                   |- 8 edges (3*8=24 lines)
    New York                              |
    Tokyo                                 |
    2500                                  |
    Tokyo                                 |
    Paris                                 |
    1500                                  |
    Sao Paolo                             |
    Cairo                                 |
    2000                                  |
    Sao Paolo                             |
    New York                              |
    2000        <-------------------------/
    
    cities = Graph()
    cities.add_vertex("London")
    cities.add_vertex("Paris")
    cities.add_vertex("Tokyo")
    cities.add_vertex("New York")
    cities.add_vertex("Las Vegas")
    cities.add_vertex("Sao Paolo")
    cities.add_vertex("Cairo")
    cities.add_edge("London","Paris",100)
    cities.add_edge("London","New York",400)
    cities.add_edge("Paris","London",100)
    cities.add_edge("New York","London",450)
    cities.add_edge("New York","Tokyo",2500)
    cities.add_edge("Tokyo","Paris",1500)
    cities.add_edge("Sao Paolo","Cairo",2000)
    cities.add_edge("Sao Paolo","New York",2000)
    '''
    f = open(filename, "r")
    graph = Graph()
    vertices_num = int(f.readline())
    empty = 0
    while vertices_num != empty:
        city = f.readline().strip()
        graph.add_vertex(city)
        vertices_num -= 1
    edge_num = int(f.readline())
    while edge_num != empty:
        vertex = f.readline().strip()
        neighbour = f.readline().strip()
        e_data = int(f.readline())
        graph.add_edge(vertex, neighbour, e_data)
        edge_num -= 1
    f.close()
    return graph


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
        l_path = 0
        pos_vertex = 0
        pos_neighbour = 1        
        for i in range(len(new_path) - 1):
            l_path += cities.get_edge_data(new_path[pos_vertex],
                                           new_path[pos_neighbour])
            pos_vertex += 1
            pos_neighbour += 1
            if l_path > length:
                break
    return path

g = read_cities("cities1.txt")
check.expect("multi_path", shortest_tour(g),
                                      ["Cairo", "Sao Paolo", "New York", 
                                       "London", "Paris", "Tokyo"])

g = read_cities("empty.txt")
check.expect("no_path", shortest_tour(g), [])

g = read_cities("two_cities1.txt")
check.expect("one_path", shortest_tour(g), ["London", "New York"])

g = read_cities("multi_same_path.txt")
check.expect("multi_same_path", shortest_tour(g), ["L", "M", "N"])