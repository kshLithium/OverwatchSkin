import requests
from bs4 import BeautifulSoup

# 세션 생성
session = requests.Session()

# 로그인 후 받은 쿠키들을 설정
session.cookies.set("login.cookies", "1")
session.cookies.set("login.key", "your_login_key")

# 기본 URL 설정 (숫자 부분은 포맷팅을 통해 변경)
base_url = "https://us.battle.net/shop/en/checkout/buy/{}"

# 체크할 숫자 범위 설정 (예: 1168357 ~ 1168370)
start_number = 1168357
end_number = 1168370

# 유효한 페이지를 저장할 리스트
valid_pages = []

# 숫자 변경하며 페이지 확인
for number in range(start_number, end_number + 1):
    url = base_url.format(number)

    # 세션을 사용하여 요청
    response = session.get(url, allow_redirects=True)

    # 최종 리다이렉트된 URL 확인
    final_url = response.url
    print(f"최종 URL: {final_url}")

    # 리다이렉션된 URL이 pay/로 시작하는지 확인
    if "pay/" in final_url:
        print(f"유효한 페이지 발견: {final_url}")
        valid_pages.append(final_url)
    else:
        print(f"무효한 페이지: {url}")

# 유효한 페이지 출력
print("\n유효한 페이지들:")
for page in valid_pages:
    print(page)
