numbers = []

positive = 0
negative = 0
zero = 0

number = int(input('몇 개의 숫자를 입력하시겠습니까? >>>'))

for i in range(number) :
    a = int(input(f'{i + 1}번재 숫자를 입력하십시오 >>> '))
    numbers.append(a)
    if a > 0 :
        positive += 1
    elif a < 0 :
        negative += 1
    else :
        zero += 1

print(f'양수 : {positive}')
print(f'음수 : {negative}')
print(f'0 : {zero}')