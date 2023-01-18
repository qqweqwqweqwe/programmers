# 맞추긴 했는데 불만족스러움
# 이 문제의 핵심은 어디에 카메라를 꽂냐가 아니라 어떤 범위 안에 카메라가 존재하냐 로 접근해야했다
# 카메라의 좌표는 의미가 없다.


def solution(routes:list):
  first=-30001
  second=-30001
  count=0
  routes.sort()

  for route in routes:
    if route[0]>second:
      first=route[0]
      second=route[1]
      print(first,second)
      count+=1
    else:
      first=route[0]
      second=min(second,route[1])


  return count

solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])