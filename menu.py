import requests
import sys
from bs4 import BeautifulSoup as bs

# 달빛학사 아이디와 비밀번호를 입력하고 사용--> GUI 구현 시 따로 저장 가능하게 할 것 / 또는 실시간 입력하기


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


def get_Menu(target_num, menu_data):
    # 가져온 문자열을 자르는 부분_ 강동욱 선생님께 도움을 요청하여 작성하고, 이후 함수로 만듦
    selectMenu = menu_data[target_num-1]  # 예를 들어 0 아침이 선택되어 있다고 가정하자.
    selectMenu = str(selectMenu)  # 문자열로 변경한다.
    selectMenu = selectMenu.replace('<br/>', '|')  # <br/> 태그를 | 로 변경하여 구분자를 선언
    selectMenu = selectMenu.split('>')[1]  # 앞쪽 <td ~~~> 태그를 분리한다.
    selectMenu = selectMenu.split('</')[0]  # 뒷쪽 </td> 태그를 분리한다.
    selectMenu = selectMenu.split('|')  # 구분자로 지정한 '|' 을 기준으로 분리한다.

    for i in range(len(selectMenu)):
        selectMenu[i] = selectMenu[i].strip()  # 공백이 있을 경우가 있기 때문에 제거

    selectMenu.remove('')  # 마지막에 빈 값이 있기때문에 제거

    return selectMenu


def check_menu(ID, PW):
    LOGIN_INFO = {
        'id': ID,
        'passwd': PW
    }
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
    breakfast = get_Menu(1, use_menu_data)
    lunch = get_Menu(2, use_menu_data)
    dinner = get_Menu(3, use_menu_data)

    print(breakfast)
    print(lunch)
    print(dinner)