# 달빛학사 로그인
# 홈 화면의 식단표 불러오기
# 아침/점심/저녁별로 자료구조에 입력
# 가능하면 more... 로 더 들어가서 다른 날짜 것도 조회하기까지


# pip install -U beautifulsoup4
# pip install -U requests

import requests
import sys
import bs4

# 달빛학사 아이디와 비밀번호를 입력하고 사용--> GUI 구현 시 따로 저장 가능하게 할 것 / 또는 실시간 입력하기
LOGIN_INFO = {
    'id' : '1703',
    'passwd' : 'kyung0207!'
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


with requests.Session() as s :
    first_page = s.get('https://go.sasa.hs.kr')
    html = first_page.text
    soup = bs4.BeautifulSoup(html,'html.parser')

# 달빛학사 계정 로그인
csrf = soup.find('input', {'name' : 'csrf_test_name'})
LOGIN_INFO.update({'csrf_test_name' :csrf['value']})
login_req = s.post('https://go.sasa.hs.kr/auth/login/', data=LOGIN_INFO)


if login_req.status_code != 200 :
    raise Exception('로그인 안됨')


print(LOGIN_INFO['id'] + " 로그인하였습니다.")
print("========================================================")
print("1. 달빛학사에서 홈 화면의 식단표를 조회합니다.")
print("2. 원하는 식사를 선택하세요.(아침/점심/저녁)")
print("3. 프로그램을 종료하고 싶으면 'exit'를 쳐주시면 됩니다.")
print("========================================================")







