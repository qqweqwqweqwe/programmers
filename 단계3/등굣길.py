# 이거 처음부터 웅덩이를 0으로 설정하면 덧셈에 영향 안줌 내가 이걸 캐치를 못했음 ㅠ 다음부턴 웅덩이 0으로 만들어서 
# 다음 연산에 영향 안주게끔
# 그리고 이거 문제 개에바인게 x,y바뀐거임 그래서 자꾸 에러났음


def solution(m, n, puddles):
  matrix=[[0 for i in range(m+1)] for j in range(n+1)]

  for puddle in puddles:
    matrix[puddle[1]][puddle[0]]='C'
  matrix[1][1]=1
  for i in range(1,n+1):
    for j in range(1,m+1):
      if i==1 and j==1:
        continue
      if matrix[i][j]=='C':
        continue
      if matrix[i-1][j]=='C' and matrix[i][j-1]=='C':
        matrix[i][j]=0
      elif matrix[i-1][j]=='C':
        matrix[i][j]=matrix[i][j-1]
      elif matrix[i][j-1]=='C':
        matrix[i][j]=matrix[i-1][j]
      else:
          matrix[i][j]=matrix[i][j-1]+matrix[i-1][j]

  return matrix[n][m]%1000000007



solution(4,3,[[2, 2]])