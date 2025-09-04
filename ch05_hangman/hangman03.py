import random

'''
''.join(반복가능 객체) method : '.' 앞에 있는 문자열을 기준으로 반복 가능 객체의 element들을 합쳐서 str로 합쳐주는 method
'''
temp = ['배', '고', '프', '다']
feeling = ''.join(temp)
print(temp)
print(feeling)
result = ''

for letter in temp :
    result += letter

print(result)
feeling2 = '/'.join(temp)
print(feeling2)
'''
이상의 예시는 display를 다시 재조합하여 str으로 바꿀 때 사용할 겁니다.
'''
# todo - 1 : 비어있는 list인 display를 선언하시요.
display = []
# todo - 2 : chosen_word의 문자 개수만큼 '_'를 display에 추가하시오.
word_list = ['apple', 'banana', 'camel']
chosen_word = random.choice(word_list)
print(chosen_word)
for _ in range(len(chosen_word)) :
    display.append('_')
# todo - 3 : 사용자가 추축을 반복할 수 있도록 while 반복문을 작성하시오. 사용자가 chosen_word의 모든 문자열들을 맞추었을 때, 즉 display에 더이상 '_'가 없을 때 반복문이 멈추도록 작성할 겁니다. 반복문 종료후 print('정답입니다!')를 출력하도록 작성하시오
while ''.join(display) != chosen_word :
    guess = input('알파벳을 입력하세요 >>> ').lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    print(display)

# todo - 4 : 정답을 보여줄 대 apple이라면 a p p l e로 출력될 수 있도록 .join() 메서드를 활용하시오.
print('정답입니다.')
print(' '.join(display))