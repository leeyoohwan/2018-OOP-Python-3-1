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

        if 'ID나 PASSWORD를 확인해주세요.' in str(login_req.text) or 'Unable to load the requested file' in str(login_req.text):
            print(0)
            return 0
        else:
            print(1)
            return 1

if __name__=='__main__':
    log_ck('1717', '')