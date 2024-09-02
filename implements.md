가격도?

가격이 낮으면 스킨아닌 제품 처리?

아이콘 이름으로 오버워치 아이템인지 구분?

아이콘이 없는 경우도 있음



멀티스레드?



이미지 해석하기? - 이미지 없는 제품들도 있음



내가 껏을 때와 진짜 에러났을 때 구분해서 처리?

except Exception 처리

에러구문 보고싶은데



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
session.cookies.set('login.key', '48b0c2aabf4ae3ff3387179c59fb5d59')

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

