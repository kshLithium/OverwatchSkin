import requests
from bs4 import BeautifulSoup

# 세션 생성
session = requests.Session()

# 로그인 쿠키 설정
session.cookies.set("_st", "your _st value")
session.cookies.set("access_token", "your access_token value")
session.cookies.set("BA-tassadar-login.key", "your BA-tassadar-login.key value")
session.cookies.set("JSESSIONID", "your JSESSIONID value")
session.cookies.set("loc", "en-us")
session.cookies.set("login.cookies", "1")
session.cookies.set("login.key", "your login.key value")
session.cookies.set("opt", "1")
session.cookies.set("web.id", "your web.id value")

# URL 설정
base_url = "https://us.battle.net/shop/en/checkout/buy/{}"

# 체크할 숫자 범위 설정
start_number = 1122000
end_number = 1123000

# 유효한 페이지를 저장할 리스트
valid_pages = []

# 숫자 변경하며 페이지 확인
for number in range(start_number, end_number + 1):
    url = base_url.format(number)

    # 세션을 사용하여 요청
    response = session.get(url, allow_redirects=True)

    # 최종 리다이렉트된 URL 확인
    final_url = response.url
    # print(f"현재 번호: {number}")

    # 리다이렉션된 URL이 pay/로 시작하는지 확인
    if "pay/" in final_url:
        print(f"유효한 페이지 : {url}")

        # 페이지 내용 파싱
        soup = BeautifulSoup(response.text, "html.parser")

        # 아이템 이름 찾기
        product_name = soup.find(
            class_="product-name meka-font-display meka-font-display--header-7"
        )

        if product_name:
            print(f"*********** {product_name.get_text(strip=True)} ***********")
        else:
            print("*******제품 이름을 찾을 수 없습니다*******")

        valid_pages.append(url)
    # else:
    #    print(f"무효한 페이지: {url}")

# 유효한 페이지 출력
print("\n유효한 페이지들:")
for page in valid_pages:
    print(page)
