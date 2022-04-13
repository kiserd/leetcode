# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # handle edge case
        if not node:
            return None
        # create some helper variables
        old_to_new = {node: Node(val=node.val)}
        # process via DFS
        s = [node]
        while s:
            curr = s.pop()
            for neighbor in curr.neighbors:
                # if first occurence, we need to create new copy node
                if neighbor not in old_to_new:
                    old_to_new[neighbor] = Node(val=neighbor.val)
                    s.append(neighbor)
                # append copy of neighbor to curr node's neighbors array
                old_to_new[curr].neighbors.append(old_to_new[neighbor])
        return old_to_new[node]
