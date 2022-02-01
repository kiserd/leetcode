"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        head = Node(node.val)
        s = [{'new': head, 'old': node}]
        visited = {}
        while len(s) != 0:
            curr = s.pop()
            new = curr['new']
            old = curr['old']
            visited[new.val] = new
            for neighbor in old.neighbors:
                if neighbor.val not in visited:
                    node = Node(neighbor.val)
                    new.neighbors.append(node)
                    s.append({'new': node, 'old': neighbor})
                else:
                    new.neighbors.append(visited[neighbor.val])
                # visited[new.val] = new
        for key in visited:
            print('val: ', visited[key].val)
            print('neighbors: ', [n.val for n in visited[key].neighbors])
            print('==================')
        return head
