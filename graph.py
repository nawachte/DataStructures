from stack_array import * #Needed for Depth First Search
from queue_array import * #Needed for Breadth First Search

class Vertex:
    '''Add additional helper methods if necessary.'''
    def __init__(self, key):
        '''Add other attributes as necessary'''
        self.id = key
        self.adjacent_to = []
        self.visited = False
        self.color = None


class Graph:
    '''Add additional helper methods if necessary.'''
    def __init__(self, filename):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.  
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertices associated 
           with the edge.'''
        self.vertexList = []
        self.vertexKeys = []
        file = open(filename, 'r')
        for line in file:
            verts = line.split()
            if verts[0] not in self.vertexKeys:
                vertex = Vertex(verts[0])
                vertex.adjacent_to.append(verts[1])
                self.vertexList.append(vertex)
                self.vertexKeys.append(verts[0])
            else:
                for i in range(len(self.vertexList)):
                    if self.vertexKeys[i] == verts[0]:
                        self.vertexList[i].adjacent_to.append(verts[1])
                        self.vertexList[i].adjacent_to = sorted(self.vertexList[i].adjacent_to, key=lambda vert: int(vert[1:]))
            if verts[1] not in self.vertexKeys:
                vertex = Vertex(verts[1])
                vertex.adjacent_to.append(verts[0])
                self.vertexList.append(vertex)
                self.vertexKeys.append(verts[1])
            else:
                for i in range(len(self.vertexList)):
                    if self.vertexKeys[i] == verts[1]:
                        self.vertexList[i].adjacent_to.append(verts[0])
                        self.vertexList[i].adjacent_to = sorted(self.vertexList[i].adjacent_to, key=lambda vert: int(vert[1:]))
        file.close()

    def add_vertex(self, key):
        '''Add vertex to graph, only if the vertex is not already in the graph.'''
        if key not in self.vertexKeys:
            self.vertexKeys.append(key)
            new = Vertex(key)
            self.vertexList.append(new)


    def get_vertex(self, key):
        '''Return the Vertex object associated with the id. If id is not in the graph, return None'''
        return self.vertexList[self.vertexKeys.index(key)]

    def add_edge(self, v1, v2):
        '''v1 and v2 are vertex id's. As this is an undirected graph, add an 
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        for item in self.vertexList:
            if item.id == v1:
                item.adjacent_to.append(v2)
            if item.id == v2:
                item.adjacent_to.append(v1)

    def get_vertices(self):
        '''Returns a list of id's representing the vertices in the graph, in ascending order'''
        vertList = self.vertexKeys
        vertList = sorted(vertList, key=lambda vert: int(vert[1:]))
        return vertList

    def conn_components(self): 
        '''Returns a list of lists.  For example, if there are three connected components 
           then you will return a list of three lists.  Each sub list will contain the 
           vertices (in ascending order) in the connected component represented by that list.
           The overall list will also be in ascending order based on the first item of each sublist.
           This method MUST use Depth First Search logic!'''
        idx = 0
        graphList = []
        while idx<len(self.vertexList):
            if self.vertexList[idx].visited == False:
                graphList.append(self.conn_helper(self.vertexList[idx]))
            idx += 1
        return graphList

    def conn_helper(self,curNode):
        for node in self.vertexList:
            node.visited = False
        nodes = self.vertexList
        nodeStack = Stack(len(nodes))
        curNode.visited = True
        nodeStack.push(curNode)
        connectedList = [curNode.id]
        while nodeStack.is_empty() == False:
            ###find next node###
            foundNext = False
            for nodestr in curNode.adjacent_to:
                node = self.get_vertex(nodestr)
                if foundNext == False and node.visited == False:
                    curNode = node
                    connectedList.append(curNode.id)
                    nodeStack.push(curNode)
                    curNode.visited = True
                    foundNext = True
            ###if there are no more nodes to visit###
            if foundNext == False:
                nodeStack.pop()
                if nodeStack.is_empty() == False:
                    curNode = nodeStack.peek()
        connectedList = sorted(connectedList,key= lambda vert: int(vert[1:]))
        return connectedList


    def is_bipartite(self):
        '''Returns True if the graph is bicolorable and False otherwise.
           This method MUST use Breadth First Search logic!'''
        for node in self.vertexList:
            node.visited = False
        graphs = self.conn_components()
        for graph in graphs:
            curNode = self.get_vertex(graph[0])
            curNode.color = 'Blue'
            nodeQueue = Queue(len(graph))
            nodeQueue.enqueue(curNode)
            while nodeQueue.is_empty() ==  False:
                curNode = nodeQueue.dequeue()
                curNode.visited = True
                for nodestr in curNode.adjacent_to:
                    node = self.get_vertex(nodestr)
                    if node.visited == False:
                        nodeQueue.enqueue(node)
                    if node.color is not curNode.color:
                        if curNode.color == 'Red':
                            node.color = 'Blue'
                        else:
                            node.color = 'Red'
                    else:
                        return False
        return True