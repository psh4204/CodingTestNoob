# -*- coding: utf-8 -*-
"""CTEST03.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13JsZjgxXfvFrHgHOFyWxlAjwoM1Xo-Co

# 구현
* 피지컬로 승부하기
* 알고리즘은 설게했는데, 구현이 먼저 풀수 있는 문제가 없을때 푸는게 좋다.
  * 쉬운 문제이지만 노가다 구현인건 먼저 풀지 말라 이소리인듯.
* 완전탐색 : 모든 경우의 수를 주저없이 다 계산하는 해결방법
* 시뮬레이션 : 한단계씩 차례대로 직접 수행해야하는 문제 유형

## 메모리 제약사항 확인

### 숫자
* 보통 정수형은 int형(4바이트),  더큰수는 long long(8바이트)
* 더큰수는 Bitinteger(클래스) : 보통 안쓴다.

### 파이썬 리스트 메모리 용량
* 1,000 개 : 4kb
* 1,000,000개 : 4mb
* 1,000,000,000개 : 40mb

* 파이썬은 동작이 매우 느리다.

### 구현문제에 접근하는 방법
* 문제길이가 길 뿐이지, 비교적 쉬운문제들이다.
* 파이썬이 구현문제에서는 강한 편이다.
* Pypy3 : python3 문법 그대로 쓰이는 프로그래밍 언어. 비교적 빠른 프로그램 실행시간을 가짐
  * Pypy3를 지원한다고 하면 시험을 Pypy3로 치자.

## 상하좌우
* 여행가 문제 : L R U D 를 통해 최종적으로 도착할 좌표 출력하기
  * 첫번째 줄 입력란은 공간의 크기 N
  * 둘째 줄 입력란엔 A가 이동할 계획서 내용이 주어진다.
  * 공간밖은 무시
  * 출력 조건 : A가 이동할 최종 목표지전 X,Y를 공백으로 구분하여 출력한다.
"""

# 내코드

# 공간크기 입력
size = int(input())
# 이동할 계획서
plans = input().split()

# L R U D 값 받기
L = [0,-1]
R = [0,1]
U = [1,0]
D = [-1,0]
moveTypes = ['L','R','U','D']

x, y = 1, 1
# 이동 계획 하나씩 확인
for i in range(len(plans)):
  tmpX, tmpY = 0, 0
  if plans[i] == 'L':
    tmpX = x + L[0]
    tmpY = y + L[1]
  elif plans[i] == 'R':
    tmpX = x + R[0]
    tmpY = y + R[1]
  elif plans[i] == 'U':
    tmpX = x + U[0]
    tmpY = y + U[1]
  elif plans[i] == 'D':
    tmpX = x + D[0]
    tmpY = y + D[1]

  if tmpX < 1 or tmpY < 1 or tmpX > size or tmpY > size:
    continue
  else:
    x, y = tmpX, tmpY

# 출력
print(x, y)

# 교재 답안
# N 입력 받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인하기
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        # 공간을 벗어나는 경우 무시
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        # 이동 수행
        x, y = nx, ny

print(x, y)

"""## 시각 
* 정수 N이 입력되면 00시 00분 N시 59분 59초 까지 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오.


"""

# # N 입력
n = int(input())

result = 0
# N시 59분 59초 에서 3이 포함되는 경우의 수 확인
# 1. 완전탐색
## 시
for h in range(n+1):
  ## 분
  for m in range(60):
    ## 초
    for s in range(60):
      if '3' in (str(h)+str(m)+str(h)):
        result += 1

# 2. 수학 계산
## 시
# for h in range(n+1):
#   if '3' in str(h):
#     result += 3600
#   else :
#     ## 분
#     for m in range(60):
#       if '3' in str(m):
#         result += 60
#       else:
#         ## 초
#         for s in range(60):
#           if '3' in str(h):
#             result += 1

# 결과
print(result)

"""## 왕실의 나이트
* 8x8 평면
* 나이트는 L자 형태로만 이동가능 정원밖으로 나갈 수 없다.
* 입력조건 : x,y -> 알파벳,n
* 나이트 이동 경우의 수 출력
  * a1 -> 2
"""

# 입력 (알파벳n) ( 열 행 )
in_data = input()

# 좌표 받기
row = int(in_data[1])
column = ord(in_data[0]) - ord('a') + 1 # ord(알파벳) : 아스키코드 변환 # chr(숫자) : 아스키코드에서 문자로 변환

# 나이트 움직임들 (리스트(튜플))
knight_moves = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]

# 경우의 수 확인
count = 0
for i in range(len(knight_moves)):
  tmpX = column +knight_moves[i][1]
  tmpY = row + knight_moves[i][0]
  if not ( tmpX > 8 or tmpY >8 or tmpX < 1 or tmpY < 1 ):
    count +=1

print(count)

"""## 게임개발
* 맵 외각은 바다(1) 
* 육지는 0
* 케릭터 는 
  * 1. 왼쪽부터 탐색후 바로왼쪽에 갈곳 있으면 1칸 움직임
  * 2. 움직이고 1번 수행
  * 3. 주위에 한번 갔던곳이나, 바다가 있는곳이면 뒤로 가는데, 바다가 있으면 멈춤

* 맵 크기 입력 : n m : n x m 칸 ( n >=3 , m<= 50 ) ( 육지 0, 바다 1 )
* 케릭터 생성칸, 바라보는 방향 ( 0 : 북, 1 : 동, 2 : 남, 3 :서 ) ( 케릭터 생성위치는 무조건 육지 )
  * x y z
* 맵 입력 ( 아. 맵생성 우리가 하는게 아니구나..ㅋㅋㅋㅋ 머야;; )

* 출력 : 밟은 땅 수


"""

# 내코드 : 푸는시간 1시간 20분 (시간도 너무 오래걸렸고, 코드도 너무 길다.)( 정확하지도 않다... ㅋㅋㅋ )

# n x m  입력
n, m = map(int, input().split())

# x y z 입력
x, y, z = map(int, input().split())

# 맵 입력
if n < 3 :
  n = 3 
if m > 50 :
  m = 50
world = [[0] * n for i in range(m)]  
for i in range((m)):
  input_world = list(map(int,input().split()))
  world[i] = input_world[:n]


result = 0 
end = 0

# 왼쪽으로 갈수으면 가고(0), 갔던칸은 표시한다(2).
def goLeft(x,y,z):
  global result
  inx = x
  iny = y
  inz = z
  inend = end
  # 움직임 및 확인(왼쪽) ( 0 : 북, 1 : 동, 2: 남, 3 : 서)
  # 북
  if z == 0:
    if world[inx-1][iny] == 0 :
      inx = inx -1
      iny = iny
      inz = 3
      world[inx][iny] = 2
      result +=1
    else:
      inz = 3
  # 동
  elif z == 1:
    if world[inx][iny+1] == 0 :
      inx = inx 
      iny = iny + 1
      inz = 0
      world[inx][iny] = 2
      result +=1
    else:
      inz = 0
  # 남
  elif z == 2 :
    if world[inx + 1][iny] == 0 :
      inx = inx + 1
      iny = iny
      inz = 1
      world[inx][iny] = 2
      result +=1
    else:
      inz = 1
  # 서
  elif z == 3 :
    if world[inx][iny -1] == 0 :
      inx = inx
      iny = iny -1
      inz = 2
      world[inx][iny] = 2
      result +=1
    else:
      inz = 2
  
  return inx, iny ,inz

def goBack(x,y,z):
  inx = x
  iny = y
  inz = z
  inend = end
  # 움직임 및 확인(왼쪽) ( 0 : 북, 1 : 동, 2: 남, 3 : 서)
  # 북
  if z == 0:
    if world[inx][iny-1] == 2 :
      inx = inx
      iny = iny-1
      world[inx][iny] = 2
    else:
      inx = inx
      iny = iny
  # 동
  elif z == 1:
    if world[inx-1][iny] == 0 :
      inx = inx-1 
      iny = iny
      world[inx][iny] = 2
    else:
      inx = inx
      iny = iny
  # 남
  elif z == 2 :
    if world[inx][iny+1] == 0 :
      inx = inx
      iny = iny+1 
      world[inx][iny] = 2
    else:
      inx = inx
      iny = iny
  # 서
  elif z == 3 :
    if world[inx+1][iny] == 0 :
      inx = inx+1
      iny = iny
      world[inx][iny] = 2
    else:
      inx = inx
      iny = iny
  
  return inx, iny ,inz

# main 문
tmpx, tmpy, tmpz = -1, -1, -1
count = 0
while end != 1 :
  x,y,z = goLeft(x,y,z)
  if tmpx == x and tmpy == z :
    if count == 4 :
      x, y, z = goBack(x,y,z)
      end = 1
    count+=1
  elif (tmpx != x or tmpx !=y) and tmpz != z : 
    tmpx = x
    tmpy = y
    tmpz = z
    count = 0


# 결과
print(world)
print(result)

"""* 코딩테스트 팁
  * 실무에서는 값에따라 예외처리를 해야함
  * 코테에서는 값이 주어지므로 예외처리를 안해도 됨
"""

# 다시 한번 풀어보자..
# 이것저것 해봤으니까 다시 해보면 무언가 되지 않을까

# n  m 입력
n, m = map(int, input().split())
# x, y, z 입력
x, y, z = map(int, input().split())

# 간 곳을 적어놓는 지도
record = [[0]*n for _ in range(m)]

# 지도 입력
world = [list(map(int,input().split()))[:n] for i in range(m)]

# 북, 동, 남, 서 의 방향의 왼쪽 좌표 (0,1,2,3)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽 turn 함수
def turnLeft():
  global z
  z += 1
  if(z >= 3):
    z = 0

# main
# 바다 or 가본곳은 1 로 표시하는것으로
result = 1
turn = 0

while True :
  turnLeft()
  nx = x + dx[z]
  ny = y + dy[z]
  # 갈수 있는 곳
  if world[nx][ny] == 0 :
    record[x][y] = 1
    x = nx
    y = ny
    result += 1
    turn = 0

  # 갈수없는곳(바다,가본곳 = 1)
  elif world[nx][ny] == 1 or record[nx][ny] == 1:
    turn += 1

  # 4회회전(어디에도 갈곳이 없을 때)
  if turn == 4 :
    
    if nz > 3 :
      
    # 뒤에 갈고 있으면 뒤로 이동
    if world[nx]][ny] == 0:
      world[x][y] == 1
      x = x+dx[nz]
      y = y+dy[nz]
      result += 1
      turn = 0

    # 뒤에 갈곳 없으면 break
    elif world[x+dx[nz]][y+dy[nz]] == 1:
      world[x][y] == 1
      break
  print(result)

print("=result=")
for i in range(m):
  print(world[i])
print(result)

# 다시다시 ( 성공.. )

# n, m
n, m = map(int,input().split())

# x,y,z
x,y,z = map(int, input().split())

# 가본곳 표시 할 맵
already_places = [[0]* n for _ in range(m)]

# 지도 만들기
world = [list(map(int,input().split()))[:n] for _ in range(m)]

# 방향 (북,동,남,서) 
# 그래프에서는  (x,y) 의 위치를 표현해서 그대로 쓰였지만
# 리스트.행열같은 표에서는 [x줄, y줄]을 표현해야해서 흡사 그래프에서 (y,x) 좌표와 같음
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 보기 함수
def seeLeft():
  global z
  z -= 1
  if z < 0 :
    z = 3

result = 1 # 방문한 칸의 수
turn_c = 0 # 회전 횟수

# main
while True:
  seeLeft()
  nx = x + dx[z]
  ny = y + dy[z]
  print(nx,ny, ":", result, turn_c)
  # 가보지 않았고, 육지인 곳 = 0
  if already_places[nx][ny] == 0 and world[nx][ny] == 0:
    already_places[x][y] = 1
    x = nx
    y = ny
    result += 1
    turn_c = 0
    continue
  # 가본곳 이나 바다인곳 = 1
  elif already_places[nx][ny] == 1 or world[nx][ny] == 1:
    turn_c += 1
  
  # 4방향 가본곳이라던지, 바다라면?
  if turn_c == 4:
    # 어우.. 좌표찾기 너무 힘들다
    # 뒤쪽방향 = 왔던 좌표 - 현재바라보는좌표(회전4회해서 방향이 돌아옴)
    lx = x - dx[z]
    ly = y - dy[z]
    # 뒤에 가본적 있는가?
    if already_places[lx][ly] == 0 :
      already_places[x][y] = 1
      x = lx
      y = ly
      break
    # 뒤에바다거나 가본적있은가?
    else :
      already_places[x][y] = 1
      break

print("---WORLD---")
for i in range(m):
  print(world[i])
print("---ROAD---")
for i in range(m):
  print(already_places[i])
print("**RESULT**")
print(result)