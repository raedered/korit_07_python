phone_number = input('전화번호를 입력하시오 >>> ')

if len(phone_number) != 13 :
    print('유효하지않은 전화번호 형식입니다.')
else :
    print(f'{phone_number} 전화번호의 중간 4자리는 {phone_number[4:8]}입니다.')