import heapq as hq


def solution(scoville, K):
    hq.heapify(scoville)
    cnt = 0
    
    while scoville:
        if scoville[0] >= K:
            return cnt
        if len(scoville) == 1:
            return -1
        first = hq.heappop(scoville)
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + 2 * second)
        cnt += 1
    
    return -1