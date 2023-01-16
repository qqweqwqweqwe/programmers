def solution(menu, order:list, k):
  for i in range(len(order)):
    order[i]=menu[order[i]]
  order.reverse()
  Time=0
  processing=[]
  maxcustomer=0
  customer=0

  while order:
    if Time==0:
      processing.append(order.pop())
      customer+=1
      
    if processing:
      processing[0]-=1
      if processing[0]==0:
        customer-=1
        processing.pop(0)

    maxcustomer=max(customer,maxcustomer)

    Time+=1
    Time=Time%k
  return maxcustomer
      
    

solution([5, 12, 30],[2, 1, 0, 0, 0, 1, 0],10)