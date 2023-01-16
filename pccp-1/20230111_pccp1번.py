
def solution(input_string):
  loner=""
  alpahcount={}
  newstr=""
  for i in range(len(input_string)):
    if newstr=="":
      newstr=newstr+input_string[i]
    else:
      if newstr[-1]==input_string[i]:
        continue
      else:
        newstr=newstr+input_string[i]

  print(newstr)

  for alpha in newstr:
    if alpha in alpahcount.keys():
      alpahcount[alpha]+=1
    else:
      alpahcount[alpha]=1
  sortalpahcount=sorted(alpahcount.keys())
  
  for key in sortalpahcount:
    if alpahcount[key]>=2:
      loner=loner+key



  if loner=="":
    return "N"
  else:
    return loner
solution("edeaaabbccd")