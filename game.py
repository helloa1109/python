import turtle
import math
import random

# 창 설정
window = turtle.Screen()
window.title("피하는 게임")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# 플레이어
player = turtle.Turtle()
player.speed(0)
player.shape("triangle")
player.color("white")
player.penup()
player.goto(0, -250)
player.direction = "stop"

# 점수
score = 0

# 점수 표시
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(-380, 260)
score_pen.write("점수: {}".format(score), align="left", font=("Courier", 24, "normal"))

# 적
enemies = []
num_of_enemies = 5

for _ in range(num_of_enemies):
    enemy = turtle.Turtle()
    enemy.speed(0)
    enemy.shape("circle")
    enemy.color("red")
    enemy.penup()
    x = random.randint(-380, 380)
    y = random.randint(100, 250)
    enemy.goto(x, y)
    enemies.append(enemy)

# 이동 함수
def move_left():
    player.direction = "left"

def move_right():
    player.direction = "right"

# 이동 처리 함수
def move():
    if player.direction == "left":
        x = player.xcor()
        x -= 3
        player.setx(x)

    if player.direction == "right":
        x = player.xcor()
        x += 3
        player.setx(x)

# 키보드 입력 처리
window.listen()
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")

# 게임 루프
while True:
    window.update()

    move()

    # 적과 플레이어 충돌 체크
    for enemy in enemies:
        if player.distance(enemy) < 20:
            player.goto(0, -250)
            player.direction = "stop"

            # 적 초기화
            for e in enemies:
                x = random.randint(-380, 380)
                y = random.randint(100, 250)
                e.goto(x, y)

            # 점수 초기화
            score = 0
            score_pen.clear()
            score_pen.write("점수: {}".format(score), align="left", font=("Courier", 24, "normal"))

    # 적 이동
    for enemy in enemies:
        y = enemy.ycor()
        y -= 1
        enemy.sety(y)

        # 적이 화면 밖으로 나갔을 때
        if enemy.ycor() < -280:
            x = random.randint(-380, 380)
            y = random.randint(100, 250)
            enemy.goto(x, y)

            # 점수 증가
            score += 10
            score_pen.clear()
            score_pen.write("점수: {}".format(score), align="left", font=("Courier", 24, "normal"))

turtle.done()
