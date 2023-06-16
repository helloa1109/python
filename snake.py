import turtle
import time
import random

delay = 0.1

# 점수
score = 0
high_score = 0

# 창 설정
window = turtle.Screen()
window.title("뱀 게임")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)

# 뱀 머리
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# 먹이
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# 점수 표시
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("점수: 0  최고 점수: 0", align="center", font=("Courier", 24, "normal"))


# 움직임 함수
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# 키보드 입력 처리
window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")

# 게임 루프
while True:
    window.update()

    # 충돌 체크
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"

        # 세그먼트 숨기기
        for segment in segments:
            segment.goto(1000, 1000)

        # 세그먼트 리스트 비우기
        segments.clear()

        # 점수 초기화
        score = 0

        # 딜레이 초기화
        delay = 0.1

        pen.clear()
        pen.write("점수: {}  최고 점수: {}".format(score, high_score), align="center",
                  font=("Courier", 24, "normal"))

    # 먹이를 먹으면
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # 새로운 세그먼트 추가
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # 딜레이 감소
        delay -= 0.001

        # 점수 업데이트
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("점수: {}  최고 점수: {}".format(score, high_score), align="center",
                  font=("Courier", 24, "normal"))

    # 세그먼트 역순으로 이동
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # 머리 이동
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # 뱀 자신과 충돌 체크
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"

            # 세그먼트 숨기기
            for segment in segments:
                segment.goto(1000, 1000)

            # 세그먼트 리스트 비우기
            segments.clear()

            # 점수 초기화
            score = 0

            # 딜레이 초기화
            delay = 0.1

            pen.clear()
            pen.write("점수: {}  최고 점수: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))

    time.sleep(delay)

turtle.done()
