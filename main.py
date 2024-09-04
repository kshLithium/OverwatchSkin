import requests
from bs4 import BeautifulSoup

# 세션 생성
session = requests.Session()

# 로그인 쿠키 설정
session.cookies.set("BA-tassadar-login.key", "your BA-tassadar-login.key")
session.cookies.set("JSESSIONID", "your JSESSIONID")

# URL 설정
base_url = "https://us.battle.net/shop/en/checkout/buy/{}"


# return value : 아이템 이름
def get_item_name(page_text):
    soup = BeautifulSoup(page_text, "html.parser")
    item_name_class = soup.find(
        class_="product-name meka-font-display meka-font-display--header-7"
    )

    # item_name 생성
    if item_name_class:
        item_name = item_name_class.get_text(strip=True)
    else:
        item_name = "item name NOT found"

    return item_name


# def get_item_price(page_text):


# return value : 리그코인, 오버워치 코인, 알 수 없는 화폐
# TODO: fix this function
def get_price_type(page_text):
    soup = BeautifulSoup(page_text, "html.parser")
    price_icon = soup.find("img", class_="virtual-currency-icon")

    if price_icon:
        if "alt" in price_icon.attrs:
            alt_value = price_icon["alt"]
            if "Overwatch Coins" in alt_value:
                return "Overwatch Coins"
            elif "Overwatch League Tokens" in alt_value:
                return "Overwatch League Tokens"
    return "Unknown Currency"


# return value : 오버워치 페이지, 오버워치가 아닌 페이지, 계속 진행 가능 여부
def get_pages(start_number, end_number):
    overwatch_pages = []
    not_overwatch_pages = []

    # 숫자 변경하며 페이지 확인
    for number in range(start_number, end_number):
        # 마지막으로 검사한 번호 저장
        if number == start_number:
            stopped_number = number
        else:
            stopped_number = number - 1

        url = base_url.format(number)

        try:
            response = session.get(url, allow_redirects=True)
            final_url = response.url
            page_text = response.text

            # URL에 pay/ 포함되어 있으면 유효한 오버워치 아이템 페이지
            if "pay/" in final_url:
                item_name = get_item_name(page_text)
                price_type = get_price_type(page_text)
                print(f"유효한 페이지 : {url}")
                print(
                    "*************** "
                    + item_name
                    + " : "
                    + price_type
                    + " ***************"
                )

                item_set = url + " --- " + item_name + " --- " + price_type
                overwatch_pages.append(item_set)

            # URL에 login/이 포함되어 있으면 로그인 세션 정보 잃음
            elif "login/" in final_url:
                print(f"로그인 세션 정보 잃음 : {final_url}")
                print("마지막으로 검사한 번호 : ", stopped_number)
                return overwatch_pages, not_overwatch_pages, False

            # URL에 purchase-eligibility/이나 region-selection/이 포함되어 있으면 오버워치 아이템이 아닐 가능성이 높음
            elif (
                "purchase-eligibility/" in final_url or "region-selection/" in final_url
            ):
                item_name = get_item_name(page_text)
                price_type = get_price_type(page_text)
                print(f"maybe not overwatch item : {final_url}")
                print(
                    "*************** "
                    + item_name
                    + " : "
                    + price_type
                    + " ***************"
                )

                item_set = url + " --- " + item_name + " --- " + price_type
                not_overwatch_pages.append(item_set)

            # 그 외의 페이지는 무효
            else:
                print(f"무효한 페이지 : {final_url}")

        except KeyboardInterrupt:
            print("****************탐색 중단***************")
            print("마지막으로 검사한 번호 : ", stopped_number)
            return overwatch_pages, not_overwatch_pages, False

        except Exception as e:
            print("****************예외 발생***************")
            print(e)
            print("마지막으로 검사한 번호 : ", stopped_number)
            return overwatch_pages, not_overwatch_pages, False

    return overwatch_pages, not_overwatch_pages, True


def main():
    start_number = int(input("검토 시작할 숫자 입력 : "))

    while True:
        # 끝 번호 설정
        end_number = start_number + 1000

        # 오버워치 페이지, 계속 진행 가능 여부 받기
        overwatch_pages, not_overwatch_pages, is_continue = get_pages(
            start_number, end_number
        )

        # 오버워치 페이지를 파일에 저장
        overwatch_file_name = "overwatch.txt"
        with open(overwatch_file_name, "a", encoding="utf-8") as file_overwatch:
            for page in overwatch_pages:
                file_overwatch.write(page + "\n")
        print(
            f"\n오버워치 아이템 {len(overwatch_pages)}개를 {overwatch_file_name}에 저장했습니다"
        )

        # 오버워치 아이템이 아닌 페이지를 파일에 저장
        not_overwatch_file_name = "not_overwatch.txt"
        with open(not_overwatch_file_name, "a", encoding="utf-8") as file_not_overwatch:
            for page in not_overwatch_pages:
                file_not_overwatch.write(page + "\n")
        print(
            f"그 외 아이템 {len(not_overwatch_pages)}개를 {not_overwatch_file_name}에 저장했습니다\n"
        )

        if not is_continue:
            print("프로그램을 종료합니다")
            break

        # 마지막 검토한 숫자에서 다시 시작
        start_number = end_number


if __name__ == "__main__":
    main()
