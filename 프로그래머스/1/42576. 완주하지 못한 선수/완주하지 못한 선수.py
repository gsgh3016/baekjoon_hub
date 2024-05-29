def solution(participant, completion):
    d = {}
    for p in participant:
        if p in d:
            d[p] += 1
        else:
            d[p] = 1
    for p in completion:
        d[p] -= 1
        if d[p] == 0:
            del d[p]
    
    for k, v in d.items():
        if v != 0:
            return k