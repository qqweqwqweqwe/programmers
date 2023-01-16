from queue import PriorityQueue
def solution(ability:list, number:int):
  answer = 0
  Que=PriorityQueue()
  while ability:
    Que.put(ability.pop())
  
  for i in range(number):
    first,second=Que.get(), Que.get()
    first,second=first+second,first+second
    Que.put(first)
    Que.put(second)

  while not Que.empty():
    answer+=Que.get()
  
    
  return answer


solution([1, 2, 3, 4],3)