'''
1. 함수의 종류
    1) 파이썬 내장 함수
    2) 메서드(method)
    3) 사용자 정의 함수
2. 함수 용어 정리
    1) 함수정의 : 사용자 함수를 새로 만드는 것을 의미(def : define)
    2) 인수(argument) : 함수에 전달할 입력핪(input)
    3) 매개변수(parameter) : 인수를 받아서 저장하는 변수를 의미
    4) 반환값 / 결과값 / 리턴값 : 함수의 출력값(output)
    5) 함수 호출(call) : 함수를 실제로 사용하는 것을 의미
3. (사용자) 함수의 형식:
def 함수_이름(매개변수1, 매개변수2):
    실행문
    return 어쩌고
변수 = 함수이름(argument1, argumant2)
'''
# 함수 정의
def display_name(name) :
    print(f'당신의 이름은 {name}입니다.')

# 함수 호출
display_name('김일')

def display_name_age(name, age) :
    print(f'당신의 이름은 {name}이고, 나이는 {age}살입니다.')

display_name_age('김이', 30)
display_name_age(age= 23, name= '김삼') # keyword argument
'''
우리가 예를 들어 input('이름을 입력하세요 >>> ')이것을 name이라는 변수에 담았다고 가정하면
name = input('이름을 입력하세요 >>> ')이라고 작성해왔습니다.

그러면 어태가지 input()이라는 파이썬 내장 함수를 사용하고 있었다고 볼 수 있습니다. 파이썬 내장 함수는 이미 정의가 되어있고, 개발자들은 함수 호출만 잘하면 되겠네요.

사용자 정의 함수의 경우 개발자 자신이 함수를 정의하고, 그후에 호출까지 하는 것까지의 과정이라고 보시면 되겠습니다.

내장 함수 예시
print() / type() / int() / float() / input()

2. 메서드(methods) : 특정 객체가 가지고 있는 함수를 의미. 특정 자료형에 포함되어있는 함수, 사실 함수와 메서드는 동일한 개념이지만, 호출 방식에 있어서의 차이가 있습니다.

함수는 독립적으로 사용 가능 / 메서드는 특정 객체를 통해서만 호출 가능
'''
# 메서드의 예시
# eng_name = input('당신의 이름을 영어로 입력하세요 >>> ').upper()
'''
이상의 코드는 함수 호출을 해서 그 결과 값을 eng_name이라는 변수에 담았다고 홀수있습니다.

그리고 어제 저희가 수업한 것처럼 input()의 결과값의 자료형은 str이었죠.
'''
# print(eng_name)
# eng_name = eng_name.upper()
# print(eng_name)
'''
그렇다면 eng_name.upper()의 경우 .upper()가 메서드에 해당하고, 해당 메서드는 str 자료형에 종속되어있다고 볼수 있겠습니다.
그리고 그 결과값을 '다시 eng_name'이라는 변수에 담았기 때문에 55번라인의 결과값과 57번라인의 결과값이 차이가 생겼네요.

함수(메서드)의 유형
'''
# 매개 변수 x / 리턴 x
def call1():
    print('[ x | x ]')

def call2(unknown_parameter):
    print('[ o | x ]')
    print(f'{unknown_parameter}라고 입력하셧나보네요')

def call3():
    print(' [x | o ]')
    return 1

def call4(unknown_parameter ,unknown_parameter2):
    print('[ o | o ]')


call1()
call2('오늘의 날씨는 시원한 편')
call2(1231423)
call3()         # 결과값 '[x | o ]' 만 나옴
print(call3())

#결과값
'''
[x | o ]
1
'''

print(call4('안녕', '하세요'))
print(call3())

'''
700 원 짜리 음료수를 뽑을 수 있는 자판기 프로그램을 구현하시오. 돈을 넣으면 몇 잔의 음료수를 뽑을 수 있는지, 그리고 잔돈은 얼마인지 모든 경우의 수를 출력하도록 합니다.

함수 정의
- 반환값 : 없음(call1 ~ call4 중 어떤 유형 일지 고민할 필요가 있습니다.)
- 함수 이름 : vending_machine()
- 매개변수 : 정수 money

코드 구성 
def vending_machine() :
    # 함수구현
    
vending_machine(3000)

실행 예
음료수 0개 잔돈, 3000원
음료수 1개 잔돈, 2300원
음료수 2개 잔돈, 1600원
음료수 3개 잔돈, 900원
음료수 4개 잔돈, 200원
'''

def vending_machine(money) :
    num = 0
    while num <= money :
        money -= 700
        num += 1
        print(f'음료수{num}개 잔돈, {money}원')

vending_machine(3000)

my_money = 3000
drink_price = 700
# # 1 for 문으로 작성
# change = my_money - (drink_price * 음료개수)
# my_money를 기준으로 음료수를 살수 있는 경우의 수를 고려했을 때 0 ~ 4 개 까지 반복문이 5번 돌아갑니다.

# for i in range(my_money // drink_price + 1) :
#     print(f'음료수{i}개 잔돈, {my_money -(drink_price * i)}원')

# 2 while 문으로 작성
# num = 0
# while my_money >= 0:
#     if my_money >= 0:
#         change = my_money-(drink_price * num)
#         print(f'음료수 개수 = {num}개, 잔돈 = {change}')
#         num += 1
#         my_money -= drink_price
#
# 일단 for 문을 기준으로 함수화시키겠습니다.
def vending_machine(money) :     # 이거 교제에 있는 무제 가지고 온건데 함수가 명사라는 점에서 별로 마음에 안듭니다.
    drink_price = 700
    for i in range(my_money // drink_price + 1) :
        print(f'음료수 개수 = {i}개, 잔돈 = {my_money - (drink_price * i)}')

vending_machine(3000)

def vending_machine2(money):
    drink_price = 700
    i = 0
    while True:
        change = money - (drink_price * i)
        if change < 0 :
            break
        print(f'음료수 개수 = {i}개, 잔돈 = {change}')

'''
예제 : 구구단 출력하기
함수 정의 :
함수 이름 : multiply
매개 변수 : 정수 n
리턴값 : 없음

함수 호출 :
multiply(dan)       # argument가 dan

실행 예
몇 단을 출력하시겠습니까?
'''

# def multiply(n) :
#     for i in range(1, 10) :
#         print(f'{n} X {i} = {n * i}')
#
# dan = int(input('몇 단을 출력하시겠습니까? >>> '))
# multiply(dan)

'''
range() 함수의 arameter 적용 순서 
1 개만 있을 때 : 한계값
2 개 있을 때 : 시작값, 한계값
3 개 있을 때 : 시작값, 한계값, 증감값 순서입니다.

그럼 현재 nultiply를 call2() 유형으로 정의 했다고 볼수 있겠습니다.

call() 유형으로 정의했을 때 

실행 예
몇 단 을 입력하시겠습니까? >>> 5

'''

def multiply () :
    dan = int(input('몇 단을 입력하시겠습니까? >>> '))     # 지역 변수(scope)
    n = 10
    for i in range(1, n) :
        print(f'{dan} X {i} = {dan * i}')

multiply()