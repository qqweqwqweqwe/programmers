def solution(command):
  direction=[[0,1],[1,0],[0,-1],[-1,0]]
  curdir=0
  curpos=[0,0]
  for c in command:
    if c=='G':
      curpos[0]+=direction[curdir][0]
      curpos[1]+=direction[curdir][1]
    elif c=='B':
      curpos[0]-=direction[curdir][0]
      curpos[1]-=direction[curdir][1]
    elif c=='R':
      curdir=(curdir+1)%4
    else:
      curdir=(curdir+3)%4
  
  return curpos

# 아 개쉽노 ㅋㅋ 5분컷
    
solution("GRGRGRB"	)