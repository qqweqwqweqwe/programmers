
from queue import Queue
'''
개병신짓함
n,m의 최댓값이 1000이라서
이딴식으로 짜게될시 재귀함수의 깊이가 괴랄하게 깊어짐
이런식 ㄴㄴ

mincount=-1
dx=[1,0,-1,0,2,0,-2,0]
dy=[0,1,0,-1,0,2,0,-2]


def dfs(x,y,matrix,jump,count,n,m,visited):
  global mincount,dx,dy
  
  if matrix[y][x]=='T':
    if mincount==-1:
      mincount=count
    else:
      mincount=min(mincount,count)
    return
  for i in range(4):
    if x+dx[i]>n-1 or x+dx[i]<0 or y+dy[i]>m-1 or y+dy[i]<0 or matrix[y+dy[i]][x+dx[i]]=='H':
      continue
    if visited[y+dy[i]][x+dx[i]]==0:
      visited[y+dy[i]][x+dx[i]]=1
      dfs(x+dx[i],y+dy[i],matrix,jump,count+1,n,m,visited)
      visited[y+dy[i]][x+dx[i]]=0
  if jump==1:
    for i in range(4,8):
      if x+dx[i]>n-1 or x+dx[i]<0 or y+dy[i]>m-1 or y+dy[i]<0 or matrix[y+dy[i]][x+dx[i]]=='H':
        continue
      if visited[y+dy[i]][x+dx[i]]==0:
        visited[y+dy[i]][x+dx[i]]=1
        dfs(x+dx[i],y+dy[i],matrix,jump-1,count+1,n,m,visited)
        visited[y+dy[i]][x+dx[i]]=0




def solution(n, m, hole):
  matrix=[[0 for i in range(n)] for j in range(m)]
  visited=[[0 for i in range(n)] for j in range(m)]
  visited[0][0]=1
  matrix[m-1][n-1]='T'
  for h in hole:
    matrix[h[1]-1][h[0]-1]='H'

  
  dfs(0,0,matrix,1,0,n,m,visited)
  return mincount


      
solution(5,4,[[1, 4], [2, 1], [2, 2], [2, 3], [2, 4], [3, 3], [4, 1], [4, 3], [5, 3]]	)
'''
# 좌표와 함께 

# 위치와 함께 갈수 있는지 아닌지
# 갈수 있는지 면 2칸씩 가는 경우 추가해주고
# 못가는 경우면 1칸씩만 가는 경우 추가해주면 된다
def solution(n, m, hole):
  answer=-1
  matrix=[[0 for i in range(n)] for j in range(m)]
  visited=[[[0 for i in range(2)] for j in range(n)] for i in range(m)]
  visited[0][0][0]=1
  visited[0][0][1]=1
  matrix[m-1][n-1]='T'
  for h in hole:
    matrix[h[1]-1][h[0]-1]='H'
  dx=[1,0,-1,0,2,0,-2,0]
  dy=[0,1,0,-1,0,2,0,-2]

    

  que=Queue()
  que.put([0,0,1,0])
  while not que.empty():
    cur=que.get()
    x=cur[0]
    y=cur[1]
    p=cur[2]
    c=cur[3]
    if matrix[y][x]=='T':
      if answer==-1:
        answer=c
      else:
        answer=min(answer,c)
    for i in range(4):
      if x+dx[i]>n-1 or x+dx[i]<0 or y+dy[i]>m-1 or y+dy[i]<0 or matrix[y+dy[i]][x+dx[i]]=='H' or visited[y+dy[i]][x+dx[i]][0]==1:
        continue
      que.put([x+dx[i],y+dy[i],p,c+1])
      visited[y+dy[i]][x+dx[i]][0]=1

    
    if p>0:
      for i in range(4,8):
        if x+dx[i]>n-1 or x+dx[i]<0 or y+dy[i]>m-1 or y+dy[i]<0 or matrix[y+dy[i]][x+dx[i]]=='H' or visited[y+dy[i]][x+dx[i]][1]==1:
          continue
        que.put([x+dx[i],y+dy[i],p-1,c+1])
        visited[y+dy[i]][x+dx[i]][1]=1

  print(answer)
  return answer
  


solution(4,4,[[2, 3], [3, 3]]	)