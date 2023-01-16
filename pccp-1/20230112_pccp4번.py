from queue import PriorityQueue

# 우선순위 큐에 배열이 들어갈때 정렬되는 기준은 배열의 첫번째 값이다...제발
# 그리고 이런거 풀때 제발!! 데이터의 범위 신경쓰면서 알고리즘 짜자...
# 무지성 대가리박기 금지!!

def solution(programs:list):
  programs.sort(key=lambda x:x[1], reverse=True)
  Que=PriorityQueue()
  Time=0
  waittimeperpoint=[0]*11
  while programs or not Que.empty():
    while programs and programs[-1][1]<=Time:
      Que.put(programs.pop())
    if Que.empty():
      Time=programs[-1][1]
    else:
      cur=Que.get()
      waittimeperpoint[cur[0]]+=Time-cur[1]
      Time+=cur[2]
  waittimeperpoint[0]=Time
  return waittimeperpoint
solution([[3, 6, 4], [4, 2, 5], [1, 0, 5], [5, 0, 5]]	)