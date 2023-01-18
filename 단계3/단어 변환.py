#시간 날때 bfs dfs 다시 공부


answer=0

def solution(begin, target, words):
  maxrep=len(begin)
  visited={}
  for word in words:
    visited[word]=0
  
  def diff(a,b):
    count=0
    for i in range(len(a)):
      if a[i]==b[i]:
        continue
      count+=1
    if count==1:
      return True
    else:
      return False

  def dfs(begin,target,words,count):
    global answer
    if count>maxrep+1:
      return
    if begin==target:
        answer=count
        return
    for word in words:
      if visited[word]==1:
        continue
      if diff(begin,word):
        visited[word]=1
        dfs(word,target,words,count+1)
        visited[word]=0


  
  dfs(begin,target,words,0)

  return answer

solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]	)