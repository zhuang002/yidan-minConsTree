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
        sz = 0
        nodeSets: set[set] = {}
        nodesAdded = 0
        sortedPaths = self.paths.sort(key=lambda x: x.length)
        for path in sortedPaths:
            set1: set = self.getNodeSet(nodeSets, path.id1)
            set2: set = self.getNodeSet(nodeSets, path.id2)
            if not set1:  # id1 is isolated
                if not set2:  # id2 is isolated
                    newSet: set = {}
                    newSet.add(path.id1)
                    newSet.add(path.id2)
                    nodeSets.add(newSet)
                    sz += path.length
                    nodesAdded += 2
                else:  # id2 is in set2
                    set2.add(path.id1)
                    sz += path.length
                    nodesAdded += 1
            else:  # id2 is in set 1
                if not set2:  # id2 is isolated
                    set1.add(path.id2)
                    sz += path.length
                    nodesAdded += 1
                else:  # id 2 is in set2
                    if set1 != set2:
                        union = set1 | set2
                        nodeSets.remove(set1)
                        nodeSets.remove(set2)
                        nodeSets.add(union)
                        sz += path.length
                    # else set1 and set 2 are the same set, we should not add the path.
            if nodesAdded == self.nNodes and len(nodeSets) == 1:
                break
        s = nodeSets.pop()
        for path in s:
            returnGraph.paths.append(path)
        returnGraph.nNodes = self.nNodes
        return returnGraph, sz

    def getNodeSet(self, nodeSets, id):
        for s in nodeSets:
            if id in s:
                return s
        return None

    def print(self):
        print(self.nNodes, len(self.paths))
        for path in self.paths:
            print(path.node1+" "+path.node2+" "+path.length)


graph = Graph()
graph.load()
graph, size = graph.kruskal()
print("size = " + size)
graph.print()
