'''
1. while 반복문
    while 다음에 나오는 조건식이 참이라면 이하의 실행문이 반복 실행됨(조건문이 False가 될 때 까지)
형식 :
while 조건식1:
    반복실행문
당현히 특정 시점에 while 반복문이 종료될 수 있도록 지정해두셔야 합니다.
'''
# n1 = 1
# while n1 < 11:
#     print(n1)
#     n1 += 1         #python에는 ++가 없습니다...

'''
기본 예제
10부터 1가지 역순으로 출력하시오.
'''

n2 = 10
while n2 > 0 :
    print (n2)
    n2 -= 1

'''
중첩 while 문 (while문 뿐만 아니라 내부에 if를 슬 수도 있겠습니다.
중접 while 및 f-string을 활용하여
기본 예제

구구단 2단부터 9단가지 출력하는 프로그램을 작성하시오.(while문 사용할것)
변수명은 dan / number로 하겠습니다.

'''

dan = 2

while dan < 10 :
    number = 1
    while number < 10 :
        print (f'{dan} X {number} = {dan * number}')
        number += 1
    dan += 1

print(number)       # 추후 설명예정