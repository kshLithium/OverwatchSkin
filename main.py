import requests
from bs4 import BeautifulSoup

# 세션 생성
session = requests.Session()

# 로그인 쿠키 설정 (필요에 따라 사용자 정의)
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


def check_pages(start_number, end_number):
    valid_pages = []

    # 숫자 변경하며 페이지 확인
    for number in range(start_number, end_number + 1):
        url = base_url.format(number)

        # 세션을 사용하여 요청
        response = session.get(url, allow_redirects=True)

        # 최종 리다이렉트된 URL 확인
        final_url = response.url

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
                item_name = product_name.get_text(strip=True)
                print("*************** " + item_name + " ***************")
            else:
                print("*******제품 이름을 찾을 수 없습니다*******")

            item = url + " --- " + item_name
            valid_pages.append(item)
        else:
            print(f"무효한 페이지 : {url}")

    return valid_pages


start_number = int(input("검토 시작할 숫자 입력 : "))

# 프로그램 실행
while True:
    # 끝 번호 설정 (시작 번호 + 1000)
    end_number = start_number + 100

    # 유효한 페이지들 찾기
    valid_pages = check_pages(start_number, end_number)

    # 유효한 페이지를 파일에 저장
    with open("foundList.txt", "a") as file:
        for page in valid_pages:
            file.write(page + "\n")

    print(f"\n유효한 페이지 {len(valid_pages)}개를 foundList.txt에 저장했습니다.\n")

    # 계속할지 여부 묻기
    continue_check = input("계속 검토하시겠습니까? (y/n) : ").strip().lower()
    if continue_check != "y":
        break

    # 마지막 검토한 숫자에서 다시 시작
    start_number = end_number + 1

print("마지막으로 검사한 번호 : ", end_number)
print("프로그램을 종료합니다")

# 프로그램 종료 후 파일 닫기
file.close()
