from queue import PriorityQueue
from queue import Queue


def solution(priorities, location):
    pq = PriorityQueue()
    q = Queue()
    target = 0
    for i, p in enumerate(priorities):
        if location == i:
            target = i
        pq.put(-p)
        q.put((p, i))
    
    cnt = 0
    while not q.empty():
        cur_high_priority = -pq.get()
        cp, ci = q.get()
        if cur_high_priority != cp:
            pq.put(-cur_high_priority)
            q.put((cp, ci))
        if cur_high_priority == cp and ci != location:
            cnt += 1
            continue
        if cur_high_priority == cp and ci == location:
            cnt += 1
            break
    
    return cnt