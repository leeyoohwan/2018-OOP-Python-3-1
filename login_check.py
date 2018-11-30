#https://github.com/kadragon/oop_python_ex/blob/master/project_ex/12_parser.py

import requests  # 웹 접속 관련 라이브러리
from bs4 import BeautifulSoup as bs  # parsing library


def log_ck(ID, PW):
    parlist=[] #파싱 결과 저장 리스트
    # 로그인이 필요한 사이트 파싱을 위한 정보 저장
    LOGIN_INFO = {
        'id': ID,
        'passwd': PW
    }

    with requests.Session() as s:
        # 로그인 페이지를 가져와서 html 로 만들어 파싱을 시도한다.
        first_page = s.get('https://go.sasa.hs.kr')
        html = first_page.text
        soup = bs(html, 'html.parser')

        csrf = soup.find('input', {'name': 'csrf_test_name'})

        # 두개의 dictionary 를 합친다.
        LOGIN_INFO.update({'csrf_test_name': csrf['value']})

        # 만들어진 로그인 데이터를 이용해서, 로그인을 시도한다.
        login_req = s.post('https://go.sasa.hs.kr/auth/login/', data=LOGIN_INFO)
        print(login_req.text)

        login_soup = bs(login_req.text, 'html.parser')

        check_login = login_soup.select('script')[0].get('alert')

        print(check_login)

        if check_login=="'ID나 PASSWORD를 확인해주세요.'":
            return False


    return True

# def sub_get_insert_time_and_press(url): #html에서 판매랭킹 1위부터 10위까지 상품 브랜드, 상품 이름, 상품 가격 가져오는 함수
#     sub_html = get_html(url)
#     sub_soup = bs4.BeautifulSoup(sub_html, 'html.parser')
#
#     for i in range(0, 1):
#         item_name = sub_soup.select('div.article_info > p.list_info')[i].get('title') #상품 이름 가져오기
#
#     return item_name

if __name__ == '__main__':
    log_ck('111', '111')