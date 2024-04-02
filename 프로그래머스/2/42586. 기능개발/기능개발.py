from queue import Queue


def solution(progresses, speeds):
    answer = []
    n = len(speeds)
    q = Queue()
    for p, s in zip(progresses, speeds):
        q.put((p, s))
    day = 1
    while not q.empty():
        p, s = q.get()
#        print(p, s)
        day_changed = False
        while p + day * s < 100:
#            print(f'cur: {p + day * s}, day: {day}')
            day += 1
            day_changed = True
        if not day_changed:
            answer[-1] += 1
        else:
            answer.append(1)
    return answer