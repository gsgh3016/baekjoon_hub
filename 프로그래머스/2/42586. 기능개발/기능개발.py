def solution(progresses, speeds):
    s1 = list(reversed(progresses))
    s2 = list(reversed(speeds))
    
    day = 1
    cnt = 0
    answer = []
    while s1:
        cur_p = s1.pop()
        cur_s = s2.pop()
        if cur_p + day * cur_s < 100:
            if cnt != 0:
                answer.append(cnt)
                cnt = 0
            s1.append(cur_p)
            s2.append(cur_s)
            day += 1
        else:
            cnt += 1
    
    answer.append(cnt)
    return answer