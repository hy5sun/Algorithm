from collections import deque

S, E = map(int, input().split())
queue = deque()
queue.append(S)
MAX = 10000
ch = [0] * (MAX+1)
cnt = [0] * (MAX+1)
ch[S] = 1
cnt[S] = 0

while queue:
    now = queue.popleft()
    if now == E:
        break
    for next in (now-1, now+1, now+5):
        if 0 < next <= MAX:
            if ch[next] == 0:
                queue.append(next)
                ch[next] = 1
                cnt[next]=cnt[now]+1
print(cnt[E])