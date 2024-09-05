가격도?

가격이 낮으면 스킨아닌 제품 처리?

아이콘 이름으로 오버워치 아이템인지 구분?

아이콘이 없는 경우도 있음?

객체화?

사이트 구현?



멀티스레드?



이미지 해석하기? - 이미지 없는 제품들도 있음


<img slot="icon" class="virtual-currency-icon" alt="Overwatch League Tokens" src="https://blz-contentstack-images.akamaized.net/v3/assets/bltf408a0557f4e4998/blt040cc2d5e8234f6d/OWL_VirtualCurrency.svg">

OWL_VirtualCurrency.svg

<img slot="icon" class="virtual-currency-icon" alt="Overwatch Coins" src="https://blz-contentstack-images.akamaized.net/v3/assets/bltf408a0557f4e4998/blta0dcc11657537871/OW2_VirtualCurrency.svg">

OW2_VirtualCurrency.svg

<img slot="icon" class="virtual-currency-icon" alt="Diablo Platinum" src="https://blz-contentstack-images.akamaized.net/v3/assets/bltf408a0557f4e4998/blt40af45aa6f7cb7dd/D4_Platinum_VirtualCurrency.png">

D4_Platinum_VirtualCurrency.png





``` python
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# 세션 생성
session = requests.Session()

# 재시도 로직 설정
retry_strategy = Retry(
    total=3,  # 최대 재시도 횟수
    status_forcelist=[429, 500, 502, 503, 504],  # 재시도할 상태 코드 목록
    allowed_methods=["HEAD", "GET", "OPTIONS"],  # 재시도할 메소드
    backoff_factor=1  # 재시도 간격 (1초, 2초, 4초 등 증가)
)

adapter = HTTPAdapter(max_retries=retry_strategy)
session.mount("https://", adapter)
session.mount("http://", adapter)

# 로그인 쿠키 설정
session.cookies.set('login.cookies', '1')
session.cookies.set('login.key', '')

# URL 설정
url = "https://us.battle.net/shop/en/checkout/buy/1168357"

try:
    # 요청 보내기
    response = session.get(url, allow_redirects=True)
    response.raise_for_status()  # 응답 오류 확인
    
    # 결과 처리
    print(f"최종 URL: {response.url}")

except requests.exceptions.RequestException as e:
    print(f"오류 발생: {e}")
```

