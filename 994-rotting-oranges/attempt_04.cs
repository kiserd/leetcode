public class Solution {
    public int OrangesRotting(int[][] grid) {
        // init hash set to keep track of cells we need to traverse
        HashSet<(int, int)> to_visit = new HashSet<(int, int)>();
        // init q
        Queue<(int, int)> q = new Queue<(int, int)>();
        for (int i = 0; i < grid.Length; i++) {
            for (int j = 0; j < grid[0].Length; j++) {
                (int, int) cell = (i, j);
                if (grid[i][j] == 1) {
                    to_visit.Add(cell);
                }
                else if (grid[i][j] == 2) {
                    q.Enqueue(cell);
                }
            }
        }
        // handle edge case where there are no fresh oranges to rot
        if (to_visit.Count == 0) {
            return 0;
        }
        // init counter and kick off BFS via q
        int res = -1;
        while (q.Count != 0) {
            // only process the number of elements in q now
            int beg_count = q.Count;
            for (int i = 0; i < beg_count; i++) {
                (int, int) curr = q.Dequeue();
                int r = curr.Item1;
                int c = curr.Item2;
                (int, int)[] adjs = {(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)};
                // give foreach a try
                foreach ((int, int) adj in adjs) {
                    if (to_visit.Contains(adj)) {
                        to_visit.Remove(adj);
                        q.Enqueue(adj);
                    }
                }
            }
            // increment res for each "step" in BFS
            res++;
        }
        if (to_visit.Count == 0) {
            return res;
        }
        return -1;
    }
}