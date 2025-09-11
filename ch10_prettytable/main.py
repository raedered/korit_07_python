'''
외부 패키지의 설치 # 1 : setting를 통한 방법
좌측 상단 메뉴버튼(햄버거) -> file -> setting(혹은 alt + ctrl + s)
좌측 리스트에서 project : 프로젝트명 으로 되어있는 부분 클릭
-> python interpreter 클릭
-> 좌상단에 + 버튼 눌러서 필요한 패키지 검색 및 패키지 설치

외부 패키지의 설치 # 2 : 터미널을 이용하는 방법
alt + f12 눌러서 터미널 켠다
pip install prettytable
'''
from prettytable import PrettyTable
from pokemon_data import pokemon_data
# PrettyTable의 객체 생성
table = PrettyTable()
table2 = PrettyTable()

table.field_names = ['이름', '나이', '주소']
table2.field_names = ['번호', '이름', '타입']
# table.add_rows(pokemon_data) # 편하게 할수 있는 명령어
for i in pokemon_data :
    table2.add_row(i)
print(table2)
