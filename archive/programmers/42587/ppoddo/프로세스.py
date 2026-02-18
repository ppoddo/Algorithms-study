from collections import deque

def solution(priorities, location):
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    active_count = 0

    while queue:
        current_queue = queue.popleft()
        has_higher_priority = False
        for q in queue:
            if current_queue[1] < q[1]:
                has_higher_priority = True
                break
        
        if has_higher_priority:
            queue.append(current_queue)
        else:
            active_count += 1
            if current_queue[0] == location:
                return active_count