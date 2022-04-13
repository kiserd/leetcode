# create a little helper class
class Path:
    def __init__(self, path):
        self.path = path
        self.prevs = {val for val in path}
class Solution:
    def leadsToDestination(self, n: int, edges, source: int, destination: int) -> bool:
        # build adjacency mapping
        adjs = {i: set() for i in range(n)}
        for st, ed in edges:
            adjs[st].add(ed)
        # attempt to return early if destination is NOT a sink
        if adjs[destination]:
            return False
        # handle edge case of src == dest
        if source == destination:
            return True
        # kick off DFS using a stack
        init_path = Path([source])
        s = [init_path]
        path_to_dest_found = False
        while s:
            curr = s.pop()
            # check whether path to another sink is found
            if curr.path[-1] != destination and not adjs[curr.path[-1]]:
                return False
            for adj in adjs[curr.path[-1]]:
                # check for cycle
                if adj in curr.prevs:
                    return False
                # handle case where we reached destination
                if adj == destination:
                    path_to_dest_found = True
                else:
                    s.append(Path(curr.path + [adj]))
        return path_to_dest_found
