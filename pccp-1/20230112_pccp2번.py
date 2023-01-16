# 이런거 풀때 viisted 함수에 매개변수로 주지말고 그냥 전역변수 선언해서 인덱스로 방문했는지 안했는지 찾는 방식으로 
# 반복문 안에서 해결할수 있으면 최대한 해결 다음 단계로 넘어가기 전에 해결

visited=[0]*10
total=0
maxtotal=0

def dfs(abillity,cursport):
  global total
  global visited
  global maxtotal
  if cursport==len(abillity[0]):
    maxtotal=max(maxtotal,total)
    return 
  
  for i in range(len(abillity)):
    if visited[i]==1:
      continue
    visited[i]=1
    total+=abillity[i][cursport]
    dfs(abillity,cursport+1)
    visited[i]=0
    total-=abillity[i][cursport]
    
  
def solution(ability):
  dfs(ability,0)
  print(maxtotal)
