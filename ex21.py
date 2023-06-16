"""
숫자를 입력하면 해당 구구단 출력
단, 2-9가 아니면 "다시 입력해주세요"
0을 입력하면 종료하면서 "프로그램 끝"
출력시 format 이용해서 출력할것
"""

while True:
    num = int(input("구구단을 출력할 숫자를 입력하세요 (2-9, 0은 종료): "))

    if num == 0:
        print("프로그램을 종료합니다.")
        break
    elif num < 2 or num > 9:
        print("2부터 9까지의 숫자를 입력해주세요.")
        continue

    print("{}단 출력".format(num))
    for i in range(1, 10):
        print("{} x {} = {}".format(num, i, num * i))
