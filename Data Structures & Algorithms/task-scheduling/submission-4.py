#ALL BY MYSELF !!! :)))
from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = Counter(tasks)
        hp = list(d.values())
        heapq.heapify_max(hp)

        delay = deque()
        cycle = 0
        while hp or delay:
            cycle += 1
            if not hp:
                cycle = delay[0][0]
            if delay and cycle == delay[0][0]:
                _, f = delay.popleft()
                heapq.heappush_max(hp, f)
            freq = heapq.heappop_max(hp)
            if freq > 1:
                delay.append([cycle+n+1, freq-1])
        return cycle




