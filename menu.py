# # 달빛학사 로그인
# # 홈 화면의 식단표 불러오기
# # 아침/점심/저녁별로 자료구조에 입력
# # 가능하면 more... 로 더 들어가서 다른 날짜 것도 조회하기까지
#
#
# # pip install -U beautifulsoup4
# # pip install -U requests
#
# import requests
# import sys
# from bs4 import BeautifulSoup as bs
#
# # 달빛학사 아이디와 비밀번호를 입력하고 사용--> GUI 구현 시 따로 저장 가능하게 할 것 / 또는 실시간 입력하기
# LOGIN_INFO = {
#     'id' : '1703',
#     'passwd' : 'kyung0207!'
# }
#
#
# def get_html(url):
#     """
#     웹 사이트 주소를 입력 받아, html tag 를 읽어들여 반환한다.
#     :param url: parsing target web url
#     :return: html tag
#     """
#     response = requests.get(url)
#     response.raise_for_status()
#
#     return response.text
#
# def starting():
#     target_num = int(input('1아침,2점심,3저녁 중 번호를 선택하세요.'))
#     if target_num == 1:
#         print("오늘 아침 식단 조회하겠습니다")
#     elif target_num == 2:
#         print("오늘 점심 식단 조회하겠습니다")
#     elif target_num == 3:
#         print("오늘 저녁 식단 조회하겠습니다")
#     elif target_num == 'exit':
#         return 0
#     else:
#         print('1~3 숫자 입력')
#         return -1
#     return target_num
#
#
# with requests.Session() as s :
#     first_page = s.get('https://go.sasa.hs.kr')
#     html = first_page.text
#     soup = bs(html,'html.parser')
#
#
# # 달빛학사 계정 로그인
# csrf = soup.find('input', {'name' : 'csrf_test_name'})
# LOGIN_INFO.update({'csrf_test_name' :csrf['value']})
# login_req = s.post('https://go.sasa.hs.kr/auth/login/', data=LOGIN_INFO)
#
#
# if login_req.status_code != 200 :
#     raise Exception('로그인 안됨')
#
#
# print(LOGIN_INFO['id'] + " 로그인하였습니다.")
# print("========================================================")
# print("1. 달빛학사에서 홈 화면의 식단표를 조회합니다.")
# print("2. 원하는 식사를 선택하세요.(1.아침/2.점심/3.저녁)")
# print("3. 프로그램을 종료하고 싶으면 'exit'를 쳐주시면 됩니다.")
# print("========================================================")
#
#
# i = True
# while i:
#     chk = starting()
#     if chk==0:
#         i=False
#     elif chk==-1:
#         continue
#
#     use_data = bs(s.get("https://go.sasa.hs.kr").text, 'html.parser')
#     use_menu_data = use_data.select('div.col-md-5 td')
#
#     print(use_menu_data)
#
#     a = []
#     k=use_menu_data[chk-1]
#     print(k)
#
#     str(k)
#     print(k)
#     k.split()
#     print(k)
#
#     # name = k.getText().split('<br/>')
#     # name = k.getText().strip()
#     # name = k.getText()
#     # name = k.getText
#
#     print("yesss")
#     a.append(k)
#
#     print(a)
#
#     a.clear()
#
#


# import requests
# import sys
# from bs4 import BeautifulSoup as bs
#
# # 달빛학사 아이디와 비밀번호를 입력하고 사용--> GUI 구현 시 따로 저장 가능하게 할 것 / 또는 실시간 입력하기
# LOGIN_INFO = {
#     'id': '1703',
#     'passwd': 'kyung0207!'
# }
#
#
# def get_html(url):
#     """
#     웹 사이트 주소를 입력 받아, html tag 를 읽어들여 반환한다.
#     :param url: parsing target web url
#     :return: html tag
#     """
#     response = requests.get(url)
#     response.raise_for_status()
#
#     return response.text
#
#
# def starting():
#     target_num = input('1아침,2점심,3저녁 중 번호를 선택하세요.')
#     if target_num == '1':
#         print("오늘 아침 식단 조회하겠습니다")
#     elif target_num == '2':
#         print("오늘 점심 식단 조회하겠습니다")
#     elif target_num == '3':
#         print("오늘 저녁 식단 조회하겠습니다")
#     elif target_num == 'exit':
#         return 4
#     else:
#         print('1~3 숫자 입력')
#         return 5
#     return int(target_num)
#
#
# with requests.Session() as s:
#     first_page = s.get('https://go.sasa.hs.kr')
#     html = first_page.text
#     soup = bs(html, 'html.parser')
#
#
# # 달빛학사 계정 로그인
# csrf = soup.find('input', {'name': 'csrf_test_name'})
# LOGIN_INFO.update({'csrf_test_name': csrf['value']})
# login_req = s.post('https://go.sasa.hs.kr/auth/login/', data=LOGIN_INFO)
#
#
# if login_req.status_code != 200:
#     raise Exception('로그인 안됨')
#
# use_data = bs(s.get("https://go.sasa.hs.kr").text, 'html.parser')
# use_menu_data = use_data.select('div#menu div.box-body table tbody tr td.menu')
#
# # use_menu_data 에는 0 아침, 1 점심, 2 저녁이 들어가 있다.
#
# target_num = 5
#
# while target_num == 5:
#     target_num = starting()
#
#     if target_num == 4:
#         sys.exit(1)
#
#
# selectMenu = use_menu_data[target_num-1]  # 예를 들어 0 아침이 선택되어 있다고 가정하자.
# selectMenu = str(selectMenu)  # 문자열로 변경한다.
# selectMenu = selectMenu.replace('<br/>', '|')  # <br/> 태그를 | 로 변경하여 구분자를 선언
# selectMenu = selectMenu.split('>')[1]  # 앞쪽 <td ~~~> 태그를 분리한다.
# selectMenu = selectMenu.split('</')[0]  # 뒷쪽 </td> 태그를 분리한다.
# selectMenu = selectMenu.split('|')  # 구분자로 지정한 '|' 을 기준으로 분리한다.
#
# for i in range(len(selectMenu)):
#     selectMenu[i] = selectMenu[i].strip()  # 공백이 있을 경우가 있기 때문에 제거
#
# selectMenu.remove('')  # 마지막에 빈 값이 있기때문에 제거
# print(selectMenu)  # 출력해보자!



import requests
import sys
from bs4 import BeautifulSoup as bs

# 달빛학사 아이디와 비밀번호를 입력하고 사용--> GUI 구현 시 따로 저장 가능하게 할 것 / 또는 실시간 입력하기
LOGIN_INFO = {
    'id': '1703',
    'passwd': 'kyung0207!'
}


def get_html(url):
    """
    웹 사이트 주소를 입력 받아, html tag 를 읽어들여 반환한다.
    :param url: parsing target web url
    :return: html tag
    """
    response = requests.get(url)
    response.raise_for_status()

    return response.text


with requests.Session() as s:
    first_page = s.get('https://go.sasa.hs.kr')
    html = first_page.text
    soup = bs(html, 'html.parser')


def get_Menu(target_num):
    # 가져온 문자열을 자르는 부분_ 강동욱 선생님께 도움을 요청하여 작성하고, 이후 함수로 만듦
    selectMenu = use_menu_data[target_num-1]  # 예를 들어 0 아침이 선택되어 있다고 가정하자.
    selectMenu = str(selectMenu)  # 문자열로 변경한다.
    selectMenu = selectMenu.replace('<br/>', '|')  # <br/> 태그를 | 로 변경하여 구분자를 선언
    selectMenu = selectMenu.split('>')[1]  # 앞쪽 <td ~~~> 태그를 분리한다.
    selectMenu = selectMenu.split('</')[0]  # 뒷쪽 </td> 태그를 분리한다.
    selectMenu = selectMenu.split('|')  # 구분자로 지정한 '|' 을 기준으로 분리한다.

    for i in range(len(selectMenu)):
        selectMenu[i] = selectMenu[i].strip()  # 공백이 있을 경우가 있기 때문에 제거

    selectMenu.remove('')  # 마지막에 빈 값이 있기때문에 제거

    return selectMenu


# 달빛학사 계정 로그인
csrf = soup.find('input', {'name': 'csrf_test_name'})
LOGIN_INFO.update({'csrf_test_name': csrf['value']})
login_req = s.post('https://go.sasa.hs.kr/auth/login/', data=LOGIN_INFO)


if login_req.status_code != 200:
    raise Exception('로그인 안됨')

use_data = bs(s.get("https://go.sasa.hs.kr").text, 'html.parser')
use_menu_data = use_data.select('div#menu div.box-body table tbody tr td.menu')

# use_menu_data 에는 0 아침, 1 점심, 2 저녁이 들어가 있다.


# 아래는 함수 작동 확인 및 출력용 코드임
breakfast = get_Menu(1)
lunch = get_Menu(2)
dinner = get_Menu(3)

print(breakfast)
print(lunch)
print(dinner)
