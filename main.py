class Path:
    node1: int
    node2: int
    length: int

    def __init__(self, id1: int, id2: int, length: int):
        if id1 < id2:
            self.node1 = id1
            self.node2 = id2
        else:
            self.node1 = id2
            self.node2 = id1

        self.length = length


class Graph:
    paths: list[Path]
    nNodes: int

    def __init__(self):
        self.paths = None
        self.nNodes = 0

    def load(self) -> None:
        self.paths = []
        self.nNodes, nPaths = map(int, input().split())
        for i in range(nPaths):
            id1, id2, length = map(int, input().split())
            path = Path(id1, id2, length)
            self.paths.append(path)

    def kruskal(self):
        returnGraph = Graph()
        returnGraph.paths = []
        sz = 0
        nodeSets: list[set[Path]] = []
        nodesAdded = 0
        sortedPaths = sorted(self.paths, key=lambda x: x.length)
        for path in sortedPaths:
            set1: set = self.getNodeSet(nodeSets, path.node1)
            set2: set = self.getNodeSet(nodeSets, path.node2)
            if not set1:  # id1 is isolated
                if not set2:  # id2 is isolated
                    newSet: set = set()
                    newSet.add(path.node1)
                    newSet.add(path.node2)
                    nodeSets.append(newSet)
                    returnGraph.paths.append(path)
                    sz += path.length
                    nodesAdded += 2
                else:  # id2 is in set2
                    set2.add(path.node1)
                    sz += path.length
                    nodesAdded += 1
            else:  # id2 is in set 1
                if not set2:  # id2 is isolated
                    set1.add(path.node2)
                    returnGraph.paths.append(path)
                    sz += path.length
                    nodesAdded += 1
                else:  # id 2 is in set2
                    if set1 != set2:
                        union = set1 | set2
                        nodeSets.remove(set1)
                        nodeSets.remove(set2)
                        nodeSets.append(union)
                        returnGraph.paths.append(path)
                        sz += path.length
                    # else set1 and set 2 are the same set, we should not add the path.
            if nodesAdded == self.nNodes and len(nodeSets) == 1:
                break

        returnGraph.nNodes = self.nNodes
        returnGraph.paths.sort(key=lambda x: (x.node1, x.node2))
        return returnGraph, sz

    def getNodeSet(self, nodeSets, id):
        for s in nodeSets:
            if id in s:
                return s
        return None

    def print(self):
        print(self.nNodes, len(self.paths))
        for path in self.paths:
            print(str(path.node1)+" "+str(path.node2)+" "+str(path.length))


graph = Graph()
graph.load()
graph, size = graph.kruskal()
print("size = " + str(size))
graph.print()
