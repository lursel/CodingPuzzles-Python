dictmap = {}

class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

def cloneGraph(node):
    global dictmap

    def dfs(input, map):
        if input in map:
            return map[input]
        output = UndirectedGraphNode(input.label)
        map[input] = output
        for neighbor in input.neighbors:
            output.neighbors.append(dfs(neighbor, map))
        return output

    if node == None:
        return None

    return dfs(node, dictmap)