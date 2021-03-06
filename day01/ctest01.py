# -*- coding: utf-8 -*-
"""CTEST01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vgY9LQF0lIa4ErwfRo7uTqiUzeNTx-vn

# 그리디
* 탐욕 알고리즘
* 가장 좋은 것을 먼저 고른다.
"""


n = 1260
count = 0

# 큰 단위의 화폐부터 차례로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types :
  count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동선의 개수 세기
  # // 연산자 : 나눈후 정수만 return
  n %= coin

print(count)

n = 1530
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
  count += n // coin
  n %= coin

print(count)

"""---
# 파이썬 부족한 문법 노트

# 리스트 컴프리헨션
  * [ '넣을 변수' '루프' '조건문' ]
  * 2차원 리스트 선언시 필수다. 정확하고 손쉽기 때문
"""

# 0부터 19까지 수 중에서 홀수만 포함하는 리스트
## [ '넣을 변수' '루프' ]
array = [i for i in range(20) if i % 2 == 1]

print(array)

# 2차원 리스트 선언시 필수다.
x = 3
y = 4
array2D = [[0] * x for _ in range(y)]

print(array2D)

"""* 리스트 관련 기타 메소드"""

a = [1, 4, 3, 5, 1, 2, 6]
print("기본리스트\t\t:", a)

# 리스트에 원소 삽입
a.append(2)
print("삽입\t\t\t:", a)

# 오름차순 정렬
a.sort()
print("오름차순 정렬\t\t:", a)

# 내림차순 정렬
a.sort(reverse = True)
print("내림차순 정렬\t\t:", a)

# 리스트 원소 뒤집기
a.reverse()
print("원소 뒤집기\t\t:", a)

# 특정 인덱스에 데이터 추가
a.insert(2,3)
print("인덱스 2에 3추가\t:",a)

# 특정 값이 데이터 개수 세기
print("값이 3인 데이터 개수\t:", a.count(3))

# 특정 값 데이터 삭제 , 단 한번 실행됨
a.remove(1)
print("값이 1인 데이터 삭제\t:", a)

"""* insert, append, remove 는 시간복잡도가 O(N) = 무겁다
* remove_all : 해당 수 한번에 삭제 후 값  return
  * 기본 함수로 제공 안됨.
  * remove_set 지정을 해서 그 값만 빼고 리스트를 다시 만들어보자.
"""

# 모든 3,5를 삭제하고 싶다.
a = [1, 4, 3, 5, 4, 2, 3, 6, 5, 5, 1, 2, 6]
remove_set = [3, 5]
result = [i for i in a if i not in remove_set]
print(result)

a = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
remove_set = [1,3,5,7,9]
result = [i for i in a if i not in remove_set]
print(result)

"""# 문자열 연산
* 문자열에 양의 정수 n을 곱하면 n번 겹쳐짐
"""

a = "시환"
print(a*3)
a *= 4
print(a)

"""* 문자열도 리스트 처럼 슬라이싱 가능"""

print(a[2:4])

"""# 튜플
* (튜플) 은 [리스트]와 유사하다.
* 튜플은 값이 변하지 않는다는 차이만 가짐.
* 다익스트라 최단 경로 알고리즘에서 (비용, 노드번호)이렇게 사용된다.

# 사전자료형_딕셔너리
* key 와 value 한쌍의 데이터로 가지는 자료형이다.
* 리스트 보다 더 빠르다.(리스트가 그냥 느리다)
"""

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'

print(data)

"""* 특정 원소를 검사할땐 리스트문 처럼 '원소 in 사전' 으로 사용가능"""

if '사과' in data:
  print("'사과'를 키로 가지고 있는 데이터가 존재합니다.")

"""* keys() : 키값 만 받아와서 리스트로 return
* values() : value값 만 받아와서 리스트로 return
"""

keyInData = data.keys()
valInData = data.values()
print(keyInData)
print(valInData)

"""# 집합자료형 set
* set(리스트,문자열)을 관리할 수 있는 자료형
* 규칙 : 중복금지, 순서없음
* 특정한 데이터가 이미 등장한적있는지 여부를 체크할때 매우 효과적

"""

# 초기화 방법1
data = set([1,1,2,2,3,4,5,6,6])
print(data)

# 초기화 방법2
data = {1,1,2,2,3,4,5,6,6}
print(data)

"""* 합집합(|), 교집합(&), 차집합(-), 연산"""

a = set([1,2,3,4,5])
b = set([3,4,5,6,7])

print(a,b)
print("합집합 :", a|b)
print("교집합 :", a&b)
print("차집합 :", a-b)

"""* add() : 원소 하나 추가
* update() : 한번에 여러 값 추가
* remove() : 특정 값 제거
"""

data = set([1,2,3])
print(data)

# 새로운 원소 추가
data.add(4)
print(a)

# 새로운 원소 여러 개 추가
data.update([5,6])
print(data)

# 특정 한 값 갖는 원소 삭제
data.remove(3)
print(data)

"""# 조건문
* 기타연산자 ( in, not in )
  * 리스트, 튜플, 문자열, 사전 에서 사용
"""

a = [1,2,3,4,5,6,7]
remove_set = [1,5,7]

result = [i for i in a if i not in remove_set]
print(result)

"""* if else 문을 한줄로 요앿해서 사용가능
  * 'return값' 'if문' 'elif문' 'else 문'
"""

# if ~ else 문을 한줄로 요약해서 사용가능
score = 85
result = "Success" if score >= 75 else "Fail"
print(result)

"""# 입출력
* 입력은 input() 
  * 문자열로 받기 때문에 타입캐스팅 필요
* 여러 값을 받을 땐
  *  list(map(int,input().split())) 사용하기
    * input 을 받으면, split으로 공백에 맞게 나누고, map을 이용하여 int형으로 변수가 적용되어 list에 적용된다.
  * int(input()) 은 줄바꿈 용도이다.
"""

# 데이터 개수 입력
n = int(input())
# 각 데이터를 공백으로 구분하여 입력
## map(적용시킬함수, 적용시킬 값) : 값에 하나 하나 함수를 적용시켜 map 변수로 줌
### list() 로 리스트화 시켰음
data = list(map(int,input().split()))

data.sort(reverse = True)
print(data)

"""* input 은 너무 느리다.
* sys.stdin.readline() 함수를 사용해보자
  * 필요에 따라 사이드 공백을 제거해야한다.
    * strip([char]) : 인자로 전달된 문자를 String 왼쪽과 오른쪽에서 제거
    * lstrip([char]) : 인자로 전달된 문자를 String 왼쪽에서 제거
    * rstrip([char]) : 인자로 전달된 문자를 String의 오른쪽에서 제거
  * 마지막줄 enter 를 삭제해야하기 때문에, rstrip()을 꼭 써야한다. 
  * readline()은 colab에서 사용이 안되넹..

"""

import sys
data = sys.stdin.readline().rstrip()
print(data)

data = list(map(int,sys.stdin.readline().rstrip().split()))
data.sort(reverse=True)

print(data)

"""* 출력은 print() 사용
  * 콤마(,)를 통해 값들이 구분지어지는데 이때 띄어쓰기로 구분되어 출력된다.
  * python3.6  이상부너 f-string문법 추가
    * value = 123
     // print(f"궁시렁 {value} 궁시렁")
    // 출력 > 궁시렁 123 궁시렁 
"""

value = 123
print(f"궁시렁 {value} 궁시렁")

"""# 주요 라이브러리의 문법과 유의점
* 반드시 알아야 하는 라이브러리는 6종
  * 내장함수
  * itertools : 반복되는 형태의 데이터를 어리하는 기능 제공
  * heapq : 힙(Heap) 기능을 제공하는 라이브러리. 우선순위 큐 기능을 구현하기 위해 사용
  * bisect : 이진탐색(Binary Search) 기능을 제공하는 라이브러리
  * collections : 덱(deque), 카운터(Counter) 등 유용한 자료구조를 포함하고 있는 라이브러리
  * math : 수학적 기능을 제공. 펙토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수부터 파이(pi)와 같은 상수를 포함하고 있다.

## 내장함수
"""

# sum()
result = sum([1,2,3,4,5])
print(result)

# min()
result = min([1,2,3,4,5])
print(result)

# max()
result = max([1,2,3,4,5])
print(result)

# eval() : 그 함수를 실행한다, ㄹㅇ 함수이름(메소드)하면 바로실행
# 여기에서는 문자열로 들어온 수학계산할때 사용
result = eval("(3+5)*7")
print(result)

# sorted() : iterable 객체가 들어왔을때 정렬된 결과를 반환
result = sorted([1,2,3,4,5])
print(result)
result = sorted([1,2,3,4,5], reverse = True)
print(result)

# key값을 이용해 정렬 할 수도 있음
result = sorted([('홍길동', 35),('이순신', 75), ('박시환', 25)], key = lambda x:x[1])
print(result)
result = sorted([('홍길동', 35),('이순신', 75), ('박시환', 25)], key = lambda x:x[0], reverse = True)
print(result)

"""## itertools
* 반복데이터 처리기능 라이브러리
* permutations : 리스트같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)을 계산해준다.
  * permutations 는 클래스이기 때문에 초기화 이후에는 리스트 자료형으로 변환하여 사용
450p 책갈피
"""

from itertools import permutations
data = ['A','B','C']
# 리스트 데이터 중에서 3개를 뽑아 나열하는 모든경우 출력
result = list(permutations(data,3))

print(result)

"""* combinations는 순서고나계업시 나열하는 모든 경우(조합)"""

from itertools import combinations

data = ['A','B','C']
result = list(combinations(data,2))

print(result)

"""* product는 permutations와 같이 리스트와 같은 원소들을 중복된 값을 포함하여 나열하는 것 (순열)"""

from itertools import product

data = ['A','B','C']
result = list(product(data,repeat=2))

print(result)

"""* combinations_with_replacement 는 combinations(조합)하는데 중복이 되게 조합한다."""

from itertools import combinations_with_replacement

data = ['A','B','C']
result = list(combinations_with_replacement(data, 2))

print(result)

"""## heapq
* 힙이 가능한 라이브러리
* 우선순위 큐기능 구현 시 사용
* 파이썬에선 힙에 단순히 값을 넣었다 빼는것만으로도 오름차순 정렬이 완료됨
  * 데이터의 최소값부터 가져오기 때문에
  * heapq.heappush : 힙 삽입
  * heapq.heappop : 힙 제거
"""

import heapq

def headsort(iterable):
  h = []
  result = []
  # 모든 원소를 차례대로 힙에 삽인
  for value in iterable:
    heapq.heappush(h, value)
  # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
  for i in range(len(h)):
    result.append(heapq.heappop(h))
  return result

result = headsort([1,4,5,6,7,8,2,3,4,5,0])
print(result)

"""* python에선 최대힙을 제공하지 않는다.
* 원소의 부호를 바꿈으로써 내림차순으로 정렬 가능하다.
"""

import heapq

def headsort(iterable):
  h = []
  result = []
  for value in iterable:
    heapq.heappush(h, -value)
  for i in range(len(h)):
    result.append(-heapq.heappop(h))
  return result

result = headsort([1,4,5,6,7,8,2,3,4,5,0])
print(result)

"""## bisect
* 이진탐색을 쉽게 구현할 수 있도록 해주는 라이브러리
* '정렬된 배열'에서 특정한 원소를 찾아야 할때 매우 효과적
* bisect_left(a,x) : 정렬된 순서를 유지하면서 리스브트 a에 삽입할 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
* bisect_right(a,x) : 정렬된 순서를 유지하면서 리스브트 a에 삽입할 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드
"""

from bisect import bisect_left, bisect_right

a = [1,2,4,4,8]
x = 4

print(bisect_left(a,x))
print(bisect_right(a,x))

"""* 정렬된 리스트에서 값이 특정 범위에 속하는 원소의 개수를 구하고자 할때 효과적이다.
* count_by_range(a,left_value,right_value)
"""

from bisect import bisect_left, bisect_right

#  값이 [left_value, rifht_value]인 데이터의 개수를 바환하는 함수
def count_by_range(a, left_value, right_value):
  right_index = bisect_right(a, right_value)
  left_index = bisect_left(a, left_value)
  return right_index - left_index

a = [1,2,3,4,5,5,5,5,5,6,7,8,8,9]

print(count_by_range(a,5,5))
print(count_by_range(a,-1,8))

"""## collections
* deque
  * 더블큐
  * 가장 앞원소, 가장 뒤 원소 관련한것 중에 가장 효율적 
"""

from collections import deque
data = deque([2,3,4])
data.appendleft(1) # 첫번째 원소에 추가
data.append(5) # 마지막 원소에 추가

print(data)
print(list(data)) # 자료형 리스트 변환

data.popleft() # 첫번째 원소 제가
data.pop() # 마지막 원소 제거

print(data)
print(list(data)) # 자료형 리스트 변환

"""* Counter 는 등장횟수를 세는 기능을 제공한다.
* iterable 객체가 주어졌을 때, 해당 객체 내부의 원소가 몇번씩 등장했는지 알려준다.

"""

from collections import Counter

counter = Counter(['red','blue', 'red', 'green','blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter))

"""## math
* 팩토리얼, 제곱근, 최대공약수(GCD) 등 제공

"""

import math

# 5! : 5팩토리얼

print(math.factorial(5))

import math

# 루트 7. 7 제곱근

print(math.sqrt(7))

import math

# 최대공약수(GCD)

print(math.gcd(21,14))

import math

#  파이, 자연상수e

print(math.pi)
print(math.e)