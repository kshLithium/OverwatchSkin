def convert_to_markdown_format(input_text):
    # 입력 텍스트를 줄 단위로 분리
    lines = input_text.strip().split("\n")

    # 변환된 텍스트를 저장할 리스트
    markdown_lines = []

    for line in lines:
        # 각 줄을 링크와 설명으로 분리
        link, description = line.split(" --- ")
        # markdown 형식으로 변환하여 리스트에 추가
        markdown_line = f"- [{description}]({link})"
        markdown_lines.append(markdown_line)

    # 리스트를 문자열로 결합하여 출력
    return "\n".join(markdown_lines)


# 예시 입력 텍스트
input_text = """
https://us.battle.net/shop/en/checkout/buy/1314606 --- Zenyatta - Overwatch World Cup Away
https://us.battle.net/shop/en/checkout/buy/1314607 --- Zenyatta - Overwatch World Cup Home
https://us.battle.net/shop/en/checkout/buy/879210 --- Zenyatta - Philadelphia Fusion
https://us.battle.net/shop/en/checkout/buy/879260 --- Zenyatta - Boston Uprising
https://us.battle.net/shop/en/checkout/buy/879301 --- Zenyatta - Dallas Fuel
https://us.battle.net/shop/en/checkout/buy/879333 --- Zenyatta - London Spitfire
https://us.battle.net/shop/en/checkout/buy/879347 --- Zenyatta - Los Angeles Gladiators
https://us.battle.net/shop/en/checkout/buy/879407 --- Zenyatta - Houston Outlaws
https://us.battle.net/shop/en/checkout/buy/879432 --- Zenyatta - New York Excelsior
https://us.battle.net/shop/en/checkout/buy/879483 --- Zenyatta - Seoul Dynasty
https://us.battle.net/shop/en/checkout/buy/879517 --- Zenyatta - Shanghai Dragons
https://us.battle.net/shop/en/checkout/buy/879828 --- Zenyatta - San Francisco Shock
https://us.battle.net/shop/en/checkout/buy/879922 --- Zenyatta - Los Angeles Valiant
https://us.battle.net/shop/en/checkout/buy/880888 --- Zenyatta - Guangzhou Charge
https://us.battle.net/shop/en/checkout/buy/880945 --- Zenyatta - Hangzhou Spark
https://us.battle.net/shop/en/checkout/buy/880980 --- Zenyatta - Paris Eternal
https://us.battle.net/shop/en/checkout/buy/881055 --- Zenyatta - Toronto Defiant
https://us.battle.net/shop/en/checkout/buy/881110 --- Zenyatta - Vancouver Titans
https://us.battle.net/shop/en/checkout/buy/881168 --- Zenyatta - Washington Justice
https://us.battle.net/shop/en/checkout/buy/881229 --- Zenyatta - Atlanta Reign
https://us.battle.net/shop/en/checkout/buy/881894 --- Zenyatta - Florida Mayhem
"""

# 함수 실행 및 결과 출력
converted_text = convert_to_markdown_format(input_text)
print(converted_text)
