'''
python 대표 collection 종류
1. list 리스트 : 추가 / 수정 / 삭제가 언제나 가능
2. tuple 튜플 : 추가 / 수정 / 삭제가 불가능
3. set 세트 : 중복된 값의 저장이 불가능 / 순서 없음
4. dict 딕셔너리 : 키 + 값으로 관리
'''
# list_example = [30, 40, '김이', [100, '김삼']]
# tuple_example = (10, 20, 30, '김사')
# set_example = {100, 200, 300, 400, '김오'}
# dictionary_example = {'이름' : '김일', '나이' : 20, '학교' : '코리아아이티'}
#
# print(list_example)
# print(tuple_example)
# print(set_example)
# print(dictionary_example)
'''
1. list
    어러 값을 저장할 때 가장 많이 사용. 자료형이 서로 다르더라도 하나의 리스트에 저장 가능. 하나의 배열(파이썬에서 리스트와 비슷한 개념)에 동일한 자료형 만을 저장할 수 있는 C, Java에 비해 python이 가지는 장점 중 하나 (근데 JS는 또 다향한 자료형이 배열에 저장되긴 합니다.)
'''
# list의 선언 및 초기화
# li1 = [1, 2, 3, '김사']
'''
    1-1. list의 index / slice
        list는 str와 동일한 방식의 index / slicing을 지원
        1) 인덱스 / 마이너스 인덱스
'''
# print(li1[0])
# print(li1[1])
# print(li1[2])
# print(li1[3])
# print(li1[-1])
# print(li1[-2])
# print(li1[-3])
# print(li1[-4])
'''
    2) slicing
    str의 슬라이싱과 같이 '시작인덱스:종료인덱스:증감값'으로 이루어져있음.
'''
# li2 = [100, 3.14, 'hello']          # list 선언 및 초기화 방법 # 1
# li3 = list( [4, 5, 6, 7, 8, 9, 0])  # list 선언 및 초기화 방법 # 2
# print(li3[0:4:2])   # 0 번지부터 4번지 앞까지, 2씩 증가시키면서.  # 결과값 : [4, 6]
'''
41 번 라인의 코드를 Java 버전으로 생각해보면
String strExample = new String("안녕하세요"); 와 같겠네요
String strExample = "안녕핫에ㅛ" 하면 되는데 굳이 어렵게 쓰는거.
    3) list element의 추가와 삭제
        list에 새로운 요소를 추가할 때는 어제 한 것 처럼 .append() / .insert()
         'method'를 사용할 수 있습니다.
        기존 요소를 삭제할 때는 .pop() 메서드를 사용합니다.
        
        .append() - 항상 마지막 인덱스에 element를 추가
        .insert(위치, 값) - 정해진위치(인덱스)해당값 추가
        
'''
# scores = [30, 40, 50]
# print(scores)
# scores.append(100)
# print(scores)
# scores.insert(0, 90)
# print(scores)
# '''
#             .pop()의 경우 빈 괄호로 사용하게 되면(call3()유형이라면) 맨 마지막 요소가 삭제됨.
#             .pop(인덱스넘버)로 작성하면 해당 인덱스의 마지막 요소를 삭제함.
# '''
# print(scores.pop()) # 근데 .pop()은 call3() 유형입니다. 즉 return값이 있는데, 그 삭제한 element가 return되기 때문에 print(scores.pop())은 현제 scores의 맨마지막 element인 100이 콘 솔에 출력됩니다.
# print(scores.pop(0))
'''
교재엘 없는 삭제 메서드 : .remove(값)을 사용하면 list 내에 해당 값을 차자 삭제함(그러니까 argument로 인덱스 넘버를 요구하는게 아니라 측정 데이터를 요구한다고 볼수 있습니다.
'''
# print(scores.remove(50))
# print(scores)
'''
li4 리스트를 선언하고, 1부터 10까지 집어 넣어 보세요
print(li4) 결과값은 [1,2,3,4,5,6,7,8,9,10]
'''
# li4 = []
# for i in range(10) :
#     li4.append(i + 1)
# print(li4)

'''
각 list 내의 element들을 뽑아내서 *2씩 시키겟습니다.
일반 for문 형식으로 한번
enhanced for문 형식으로 한 번 해서 첫 번째 element 4가 되어야 겠습니다.
'''

# for i in range(len(li4)) :
#     new_element = li4[i]*2                # 이거 element를 봅아서 2를 곱한거지 li4를 바꾼게 아니라서 그렇습니다.
# print(li4)

# 향상된 for문의 성격 -> 읽기는 되는데 쓰기가 골치아프다
# n = 0
# for element in li4:
#     li4[n] = element*2
#     n += 1
# print(li4)
# 사실항 list의 element들에게 동일한 연산을 일괄적으로 적용하는 method가 있기 때문에 추후 설명할 예정입니다. 백엔드에서보다 프론트에서 더 많이 쓰여서 예시는 이후 수업
'''
    2. tuple 튜플
        저장된 값을 변경할 수 없는 list라고 생각하시면 됩니다. 순서는 있기 때문에 inde 넘버와 slicing은 가능하지만 저장된 값 이외에는 추가 / 수정 / 삭제가 불가능.
        
        소괄호를 통해서 생성
'''
# tu1 = (1,2,3)               # 튜플 생성 방법 # 1
# tu2 = tuple((4, 5, 6))      # 튜플 생성 방법 # 2
# tu3 = 7, 8, 9               # 튜플 생성 방법 # 3
#
# a, b, c = 7, 8, 9           # 복수의 변수 선언 및 초기화 방법 -> 즉 변수 개수와 데이터 개수가 같으면 가능
# print(a)
# print(b)
# print(c)
#
# tu4 = 0                     # 그럼 얘의 자료형은 뭘까요
# print(type(tu4))            # 결과값 : <class 'int'>
# # tu4라고 해서 저희는 튜플로 생각하고 변수명을 지었지만 실제로는 그냥 int 변수명이겠죠.
#
# tu5 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# print(tu5)
'''
element 추출 및 slicing은 동일하기 때문에 수업하지 않겠습니다.
마찬가지로 tuple의 특성상 element의 추가 / 수정 / 삭제가 불가능하기 때문에 수업할 일이 없겠네요.
'''

# tu6 = 'hello.', 'good morning', 'my name is', 'kim-il', 'i am', '20', 'years old'
# for word in tu6:
#         print(word.title(), end= ' ')    # 결과값 : Hello. Good Morning My Name Is Kim-Il I Am 20 Years Old
#
# print()
# print(tu6)
'''
굳이 이상의 예시를 남겨두는 이유는 우리가 배우는 collection의 개념과 내부 element의 자료형이 서로 다르다는 점입니다. tuple의 정의는 element의 추가 / 수정 /삭제가 불가능한 collection이지만, 디드둣emfdms rkrhddl rksmdgkqslek.

가공해서 tuple에 대입하는 것이 불가능하겠죠. 수정이 안되니까.

    3. set
        수학의 집합 개념. Java에서랑 같습니다.
'''
# set1 = {1, 2, 3}        # 세트 생성 방법 # 1
# set2 = set({4, 5, 6})   # 세트 생성 방법 # 2
#
# print(set1)
# print(set2)

# 궅이 # 1, 2를 나눈 이유 : 비어있는 list / tuple / set 생성방법
# li = []
# tu = ()
# se = {}

# print(type(li))     # 결과값 : <class 'list'>
# print(type(tu))     # 결과값 : <class 'tuple'>
# print(type(se))     # 결과값 : <class 'dict'>
'''
    se = {} 형태로 비어있는 set을 생성햇을 경우 se는 사실 <class 'dict'>로 나옵니다. 아직 배우지않은 dictionary 자료형으로 생성됩니다. 그래서 비어있는 set를 생성하기 위해서는 반드시 #2 방식으로 만들얼줘야합니다.
'''
# se2 = set({})
# print(type(se2)) # 결과값 : <class 'set'>
'''
    list / tuple은 index가 존재한다고 했습니다. 이 두개를 sequence 라고 하고, set / dictionary 의 경우에는 index가 없어서 비시권스라는 표현을 씁니다. 슬라이싱이 없겠네요
    
            element 관련 메서드
            1. .add() - set에 새로운 element 추가
            2. .remove() - 기존 element 삭제
            3. .discard() - 기존 element 삭제
'''
# se3 = {10, 20, 30}
# se3.add(50)
# print(se3)
# se3.remove(30)
# print(se3)

# remove() vs. discard()
# se3.remove(70)        # 오류 발생 - '값을 정확하게 입력' 해야만 한다고 했으니까요
# se3.discard(70)          # 얘는 오류 발생 안합니다. discard()는 element로 정확한 값이 없으면 그냥 종료됩니다.
# print(se3)

# 향상된 for문으로 elemant를 추출할 수는 있습니다. 순서를 보장 못해서 그렇지.
# for element in se3:
#     print(element, end=' ')

'''
    4. dict(ionay) - Java에서의 Map / JS에서의 Object / JSON과 같은 형식입니다.
    
'''
# dict1 = {
#     '이름' : '김일',
#     '나이' : 20,
#     '주소' : ['서울특별시', '마포구', '목동'],
# }
'''
    전에 수업했던 것처럼 189번 라인까지 지금 key-value pair가 있는데 189번 라인에 콤마치고 엔터치고 키-값 입력하면 번거로우니까 맨 마지막 property에 콤마 찍어주는 게 매너라고 합니다.
    
    딕셔너리 에는 인덱스는 존재하지 않지만 key를 인덱스와 유사하게 사용합니다. 즉 key를 알면 값을 확인할 수 있는 구조입니다.
'''
# list의 element 추출 반복문 작성
# li01 = [10, 20, 30, 40]
# for num in li01:
#     print(num)

#dictionary에서 같은 방식의 반복문을 활용하게 될때,
# 진짜진짜진짜 중요해서 한 번 더 말하는거 dictionary/JS Object에서 향상된 for문으로 반복문 돌리면 key가 빠져나옵니다.
# 그래서 딕셔너리명[key]로 작성해주셔야 value를 조회할 수 있습니다.
# for key in dict1:
#     print(key)
#     print(dict1[key])

# key들만 추출하는 메서드
# print(dict1.keys())             # 결과값 : dict_keys(['이름', '나이', '주소'])
# print(type(dict1.keys()))       # 결과값 : <class 'dict_keys'>

# value만 추출하는 메서드
# print(dict1.values())           # 결과값 : dict_values(['김일', 20, ['서울특별시', '마포구', '목동']])
# print(type(dict1.values()))     # 결과값 : <class 'dict_values'>

# key들만 봅아서 list를 만든다든지 / value들만 뽑아서 list를 lis야 함

# keys = list(dict1.keys())
# values = list(dict1.values())
# print(keys)                 # 그럼 이제는 인덱스로 추출하는 것이 가능하겠죠.
# print(values)

'''
그래서 collections 수업 상황에서 매우 중요한 것은 list를 배웠을 때 list만 생각할 것이 아니라 set이나 tuple, dictionary로 자료형 변경이 가능한가, 어떤식으로 가능한가, 어떨 때 써야하는가와 같이 종합적인 고려를 하는 역량이 데이터를 다룰 때 중요하다고 할 수 있겠습니다.

        1) dictionary에서 property 추가 / 삭제
'''
# dict1['직업'] = '웹 퍼블리셔'      # 기존에 없는 key를 입력하고 = value 지정하면 됩니다.
# print(dict1)
# dict1['직업'] = '웹 개발자'       # key 하나당 value는 고정이기 때문에 재대입이 이루어집니다.
# print(dict1)
# # 삭제방법
# print(dict1.pop('직업'))                 # key를 알아야지 삭제 가능 / pop()의 return 특성값은 중요합니다.
# print(dict)

'''
응용 예제

list [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]의 3번째 요소로부터 7번째 요소만 추출한 결과, 그리고 그
list에서 2번째 요소를 출력하는 프로그램을 작성하시오.

실행 예
3 번째 요소로부터 7 번째 요소 = [30, 40, 50, 60, 70]
3 번재 요소로부터 7 번째 요소 중 2번째 요소 40
'''

# li001 = []
#
# for i in range(10) :
#     li001.append((i * 10) + 10)
# list_sliced = li001[2:7]
#
# print(li001)
# print(li001[2])
# print(f'3 번째 요소로부터 7 번째 요소 = {li001[2:7:]}')
# print(f'3 번재 요소로부터 7 번째 요소 중 2번째 요소 {li001[2:7:][1]}')
#
# print(f'3 번째 요소로부터 7 번재 요소 = {list_sliced}')
# print(f'3 번재 요소로부터 7 번째 요소 중 2번째 요소 {list_sliced[1]}')

'''
사용자로부터 1에서 12사이의 월을 입력 받아, 해당 월이 며칠까지 있는지 출력하는 프로그램을 작성하시오.
(윤년은 고려 x)

실행 예
1 ~ 12 사이의 월을 입력하세요 >>> 2
2월은 28일 까지 입니다.
'''

# # 1 : dictionary 이용 방법
# # 2 : list를 이용하는데, [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]을 이용하는 방법
# # 3 : list를 이용하는데, [28, 30, 31]을 이용하는 방법


# last_date_dict = {
#     '1' : 31,
#     '2' : 28,
#     '3' : 31,
#     '4' : 30,
#     '5' : 31,
#     '6' : 30,
#     '7' : 31,
#     '8' : 31,
#     '9' : 30,
#     '10' : 31,
#     '11' : 30,
#     '12' : 31,
# }
# month = input('1 ~ 12 사이의 월을 입력하세요 >>> ')
#
# print(f'{month}월은 {last_date_dict[month]}까지 입니다.')
#
# last_date_list1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# print(f'{month}월은 {last_date_list1[int(month)-1]}까지 입니다.')
#
# last_date_list2 = [28, 30, 31]
# if month == '1' or month == '3' or month == '5' or month == '7' or month == '8' or month == '10' or month == '12':
#     print(f'{month}월은 {last_date_list2[int(month)-1]}까지 입니다.')
# elif month == '2' :
#     print(f'{month}월은 {last_date_list2[int(month)-1]}까지 입니다.')
# elif month in [4, 6, 9, 11] :
#     print(f'{month}월은 {last_date_list2[int(month)]}까지 입니다.')
# else:
#     print('잘못 입력하셧습니다.')

'''
이상의 코드 라인에서 중요한 것은 in 개념입니다.
in 뒤에는 다양한 것들이 올 수 있는데, 특히 반복가능객체(iterable)이 올 수 있다는 점입니다.
그래서
elif month_int in [ 1, 3, 5, 7, 8, 10, 12 ] :
    last_date = last_date_list2[2]
의 해석부분이 중요한데 in 다음에 임의의 list를 초기화하여 month_int가 임의의 list의 element값을 가지고 있는지 여부를 조건 검토했다고 해석할 수 있겠습니다.

(1, 3, 5, 7, 8, 10, 12) 이렇게 초기화하더라도 전혀 문제가 없겠네요. tuple로 집어넣은 사례가 되겠습니다.
'''
'''
응용 예제
수학 여행을 어디로 갈 지 결정하기 위해 학생들이 희망하는 모든 수학 여행 장소를 조사하기로 했습니다.
학생들이 원하는 장소를 입력 받아 동일한 입력을 무시하고 모든 입력을 저장하려고 합니다.
학생을 3 명으로 가정하고 실행 예와 같이 동작하는 프로그램을 작성하시오.

실행 예

희망하는 수학여행지를 입력하세요 >>> 제주
희망하는 수학여행지를 입력하세요 >>> 제주
희망하는 수학여행지를 입력하세요 >>> 민속촌

조사된 수학 여행지는 {'제주', '민속촌'}입니다
조사된 수학 여행지는 ['제주', '민속촌']입니다.
'''
# trip = []
# for i in range(3) :
#     student = input('희망하는 수학여행지를 입력하세요. >>> ')
#     trip.append(student)
# trip_set = set(trip)
# trip_list = list(trip_set)
# print(f'조사된 수학 여행지는 {trip_set}입니다.')
# print(f'조사된 수학 여행지는 {trip_list}입니다.')

'''
짝수만 추출하기

사용자로부터 임의의 양의 정수를 입력 받고, 그 정수만큼 숫자를 입력 받아 list에 저장하세요.
이 후 저장된 숫자 중 짝수만 새로운 list에 저장하여 출력하는 프로그램을 작성하세요.

실행 예
몇 개의 숫자를 입력할까요? >>> 5
1번째 숫자를 입력하세요 >>> 10
2번째 숫자를 입력하세요 >>> 15
3번째 숫자를 입력하세요 >>> 20
4번째 숫자를 입력하세요 >>> 25
5번째 숫자를 입력하세요 >>> 30
입력 받은 숫자는 [10, 15, 20, 25, 30] 입니다.
입력 받은 숫자들 중 짝수는 [10, 20, 30] 입니다.
'''
# numbers = []
# numbers2 = []
#
# number = int(input('몇 개의 숫자를 입력할까요? >>> '))
#
# for i in range(number) :
#     a = int(input(f'{i + 1}번째 숫자를 입력하세요 >>> '))
#     numbers.append(a)
#     if a % 2 == 0 :
#         numbers2.append(a)
# print(f'입력받은 숫자는 {numbers} 입니다.')
# print(f'입력받은 숫자들 중 짝수는 {numbers2} 입니다.')

'''
딕셔너리 기반의 연락처 관리

사용자로부터 3명의 이름과 전화번호를 입력 받아 딕셔너리에 저장한 뒤, 입력한 정보를 추출하는 프로그램을 작성하시오.

실행 예
1 번재 사람의 이름을 입력하세요 >>> 김일
1 번째 사람의 연락처를 입력하세요 >>> 010-1234-5678
2 번재 사람의 이름을 입력하세요 >>> 김이
2 번째 사람의 연락처를 입력하세요 >>> 010-2345-6789
3 번재 사람의 이름을 입력하세요 >>> 김삼
3 번째 사람의 연락처를 입력하세요 >>> 010-3456-7890

입력 받은 연락처는 { '김일' : '010-1234-5678', } 입니다.
'''

# dict1 = {}
# for i in range(3) :
#     name = input (f'{i + 1} 번째 사람의 이름을 입력하세요 >>> ')
#     phone_number = input (f'{i + 1} 번째 사람의 연락처를 입력하세요 >>> ')
#     dict1[name] = phone_number
#
# print(f'입력 받은 연락처는 {dict1} 입니다.')

'''
숫자를 입력한 횟수만큼 비어있는 list에 숫자를 추가하기
문제 : 비어있는 numbers1을 전언하고, 그 안에 입력 받은 횟수만큼 숫자를 추가하시오.

함수 정의 : add_numbers()
매개 변수 : 정수 n

함수 호출
add_numbers1(last_num)          # call2()유형
print(add_numbers2(last_num))   # call4()유형
'''

# numbers1 = []
# def add_numbers(n) :
#     for i in range(n) :
#         numbers1.append(i + 1)
#     print(numbers1)
#
# last_num = int(input('숫자 몇 까지 입력하시겠습니까? >>> '))
# add_numbers(last_num)
#
# numbers2 = []
#
# def add_numbers2(n) :
#     for i in range(n):
#         numbers2.append(i + 1)
#     return numbers2
#
# print(add_numbers2(last_num))
# print()
#
# hello = ['안', '녕', '하', '세', '요']
#
# def add_numbers3(n, temp_list) :
#     # 1
#     # temp_temp_list = []
#     # for i in range(n):
#     #         temp_temp_list.append(i+ 1)
#     # result = temp_temp_list + temp_list
#     # print(result)
#
#     # 2
#     for i in range(n) :
#         temp_list.insert(i, i+1)
#     print(temp_list)
#
# add_numbers3(last_num, hello)       # 결과값 : [1,2,3,4,5,6,7,8,9,10, '안','녕','하','세','요']

'''
짝수와 홀수의 개수 세기
list를 입력 받아 짝수와 홀수의 개수를 세는 함수를 작성하시오.

함수 정의
함수 이름 : count_even_odd
매개변수 : list numbers(요소는 모두 정수일것)

함수 호출
count_even_odd([1,2,3,4,5,6,7,8,9,10])

실행 예
짝수의 개수 : 5개
홀수의 개수 : 5개

'''
def count_even_odd(numbers) :
    even = 0
    odd = 0
    for i in numbers :
        if numbers % 2 == 0 :
            even += 1
        else :
            odd += 1
    print(f'짝수의 개수 : {even}')
    print(f'홀수의 개수 : {odd}')


count_even_odd([1,2,3,4,5,6,7,8,9,10])

def count_even_odd2 (numbers) :
    evens = []
    odds = []
    for number in numbers :
        if number % 2 == 0:
            evens.append(number)
        else:
            odds.append(number)
        print(f'짝수의 개수 : {len(evens)}')
        print(f'홀수의 개수 : {len(odds)}')
count_even_odd2([1,2,3,4,5,6,7,8,9,10])

def count_even_odd3(numbers) :
    evens = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    print(f'짝수의 개수 : {len(evens)}')
    print(f'홀수의 개수 : {len(evens)- len(evens)}')