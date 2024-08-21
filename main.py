import requests

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
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f"유효한 페이지 발견: {url}")
        valid_pages.append(url)
    else:
        print(f"무효한 페이지: {url}, 상태 코드: {response.status_code}")

# 유효한 페이지 출력
print("\n유효한 페이지들:")
for page in valid_pages:
    print(page)