import graph_class

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
