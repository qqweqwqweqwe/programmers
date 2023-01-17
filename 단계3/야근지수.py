import heapq

# 우선순위큐 보다 힙을 가까이 하자
# 야근을 할 필요가 없는경우, n>sum(wokrs) 인경우 그냥 0 반환 해주면 된다.
# 그리고 이거 bf로 푼애들 있는데 걔네 싹다 틀린거
def solution(n, works:list):
  answer=0
  heap=[]
  for work in works:
    heapq.heappush(heap,-work)

  while n>0:
    cur=-heapq.heappop(heap)
    cur-=1
    n-=1
    if cur==0:
      if not heap:
        return 0
      continue

    
    heapq.heappush(heap,-cur)

  while heap:
    answer+=(-heapq.heappop(heap))**2
  return answer



solution(1,[2, 1, 2])