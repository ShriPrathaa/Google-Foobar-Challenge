import heapq
def solution(grid):
    M, N = len(grid), len(grid[0])
    k=1
    q = [(1, 0, 0, k)]
    seen = set([(0, 0, k)])
    while q:
        l, r, c, kRemaining = heapq.heappop(q)
        if r == M - 1 and c == N - 1:
            return l
        for adj in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if adj[0] >= 0 and adj[0] < M and adj[1] >= 0 and adj[1] < N:
                if grid[adj[0]][adj[1]] == 1:
                    if kRemaining > 0 and (adj[0], adj[1], kRemaining - 1) not in seen:
                        heapq.heappush(q, (l + 1, adj[0], adj[1], kRemaining - 1))
                        seen.add((adj[0], adj[1], kRemaining - 1))
                elif (adj[0], adj[1], kRemaining) not in seen:
                    heapq.heappush(q, (l + 1, adj[0], adj[1], kRemaining))
                    seen.add((adj[0], adj[1], kRemaining))
    return -1
                        

