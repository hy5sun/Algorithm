from queue import PriorityQueue
n = int(input())

que = PriorityQueue(maxsize = n) #큐 초기화. 최대 크기 n

# 원소 추가
que.put(1)
que.put(8)
que.put(3)
que.put(2)

# 원수 삭제
print(que.get()) # 1
print(que.get()) # 2
print(que.get()) # 3
print(que.get()) # 8

# 다른 기준으로 원소가 정렬되기 원한다면 (우선순위, 값)의 튜플 형태로 데이터 추가 및 제거
que.put((3, 'A'))
que.put((1, 'B'))
que.put((2, 'C'))

print(que.get()[1]) # B
print(que.get()[1]) # C
print(que.get()[1]) # A