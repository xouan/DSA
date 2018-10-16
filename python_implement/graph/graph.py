from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue

def buildGraph(wordFile):
    d = {}
    g = Graph()
    with open(wordFile, 'r') as f:
        # 1 create bucket
        for line in f:
            word = line[:-1]
            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i+1:]
                if bucket in d:
                    d[bucket].append(word)
                else:
                    d[bucket] = [word]
        # 2 add vertices and edges
        for bucket in d.keys():
            for word1 in d[bucket]:
                for word2 in d[bucket]:
                    if word1 != word2:
                        g.add_edge(word1, word2)
    return g

def bfs(g, start):
    g = Graph()
    start = Vertex()
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while vertQueue.size() > 0:
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if nbr.getColor() == 'white':
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')

def traverse(y):
    x = y
    while x.getPred():
        print(x.getId())
        x = x.getPred()
    print(x.getId())

def knightGraph(bdSize):
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bd):
            nodeId = posToNodeId(row, col, bdSize)
        newPositions = genL

def posToNodeId(row, column, board_size):
    return row * board_size + column

if __name__ == '__main__':
'''
    g = Graph()
    for i in range(6):
        g.add_vertex(i)
    print(g.vert_list)
'''
traverse(g.getVertex('sage'))