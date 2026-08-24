from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = Counter(tasks)
        hp = list(d.values())
        delay = deque()
        heapq.heapify_max(hp)
        cycle = 0
        while hp or delay:
            cycle += 1
            if not hp:
                cycle = -1*delay[0][0] + n + 1 
            while delay and cycle + delay[0][0] - 1 >= n:
                _, f = delay.popleft()
                heapq.heappush_max(hp, f)
            freq = heapq.heappop_max(hp)
            if freq > 1:
                delay.append([-cycle, freq-1])
        return cycle




