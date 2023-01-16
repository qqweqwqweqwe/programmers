import math
def solution(queries):
  answer=[]
  for query in queries:
    generation=query[0]
    number=query[1]
    if generation==1:
      answer.append('Rr')
      continue
    
    block=4**generation//16

    while True:
      if number/block<=1:
        answer.append('RR')
        break
      elif number/block>3:
        answer.append('rr')
        break
      else:
        if number==1:
          answer.append("RR")
          break
        elif number==2 or number==3:
          answer.append("Rr")
          break
        elif number==4:
          answer.append('rr')
          break
        else:
          number-=(math.ceil(number/block)-1)*block
          block=block//4
  return answer

