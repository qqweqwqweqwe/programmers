from collections import deque

def solution(A:list, B:list):
  d=deque()
  result=0
  A.sort(reverse= True)
  B.sort(reverse=True)
  index=0
  for i in B:
    d.append(i)

  while d:
    cur=d.popleft()
    if A[index]>=cur:
      d.appendleft(cur)
      d.pop()
    else:
      result+=1
    index+=1


  return result

solution([2,2,2,2],[1,1,1,1]	)