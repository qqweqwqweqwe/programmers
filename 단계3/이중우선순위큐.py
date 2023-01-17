# 정답률 67퍼 짜리 치고 은근히 고전했던 문제
# length가 0이 되면 우선순위 큐가 비어있단 소리므로 최소힙 최대힙 다시 생성해주었음


from queue import PriorityQueue


def solution(operations):
  Minpq=PriorityQueue()
  Maxpq=PriorityQueue()
  a,b=0,0
  length=0
  for operation in operations:
    if length==0:
      Minpq=PriorityQueue()
      Maxpq=PriorityQueue()
    operation=operation.split(' ')
    if operation[0]=='I':
      length+=1
      op=int(operation[1])
      Minpq.put((op,op))
      Maxpq.put((-op,op))
    elif operation[0]=='D':
      if length>0:
        length-=1
        if operation[1]=='1':
          if not Maxpq.empty():
            Maxpq.get()
        elif operation[1]=='-1':
          if not Minpq.empty():
            Minpq.get()
  if length>0:
    b=Maxpq.get()[1]
    a=Minpq.get()[1]
  return [b,a]

print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]	))


