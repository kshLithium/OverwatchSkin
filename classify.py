# 지정할 캐릭터명 리스트
character_names = [
    "D.Va",
    "Doomfist",
    "Junker Queen",
    "Mauga",
    "Orisa",
    "Ramattra",
    "Reinhardt",
    "Roadhog",
    "Sigma",
    "Winston",
    "Wrecking Ball",
    "Zarya",
    "Ashe",
    "Bastion",
    "Cassidy",
    "Echo",
    "Genji",
    "Hanzo",
    "Junkrat",
    "Mei",
    "Pharah",
    "Reaper",
    "Sojourn",
    "Soldier: 76",
    "Sombra",
    "Symmetra",
    "Torbjörn",
    "Tracer",
    "Widowmaker",
    "Ana",
    "Baptiste",
    "Brigitte",
    "Illari",
    "Kiriko",
    "Lifeweaver",
    "Lúcio",
    "Mercy",
    "Moira",
    "Zenyatta",
    "Juno",
]


def classify_items(file_path, output_path, character_names):
    # 모든 캐릭터에 대한 수집된 데이터를 저장할 딕셔너리
    classified_data = {name: [] for name in character_names}

    # all.txt 파일을 읽기
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

        # 각 줄을 반복하며 캐릭터명과 매칭되는지 확인
        for line in lines:
            for character in character_names:
                if f"{character} - " in line:
                    classified_data[character].append(line.strip())
                    break  # 한 번 찾으면 더 이상 다른 캐릭터와 비교할 필요 없음

    # classify.txt 파일에 작성
    with open(output_path, "w", encoding="utf-8") as output_file:
        for character, items in classified_data.items():
            output_file.write(f"{character}\n\n")
            for item in items:
                output_file.write(f"{item}\n")
            output_file.write("\n-------------------\n\n")


def main():
    classify_items("all.txt", "classify.txt", character_names)


if __name__ == "__main__":
    main()
