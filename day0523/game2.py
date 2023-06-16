import turtle
import random
from tkinter import messagebox

# 창 설정
window = turtle.Screen()
window.title("엄준식을 피해라")
window.bgcolor("white")
window.setup(width=800, height=600)
window.tracer(0)

# 플레이어
player = turtle.Turtle()
player.speed(0)
player.shape("turtle")
player.color("black")
player.penup()
player.goto(-350, 0)
player.direction = "stop"

# 이동 함수
def move_up():
    y = player.ycor()
    y += 20
    player.sety(y)

def move_down():
    y = player.ycor()
    y -= 20
    player.sety(y)

# 키보드 입력 처리
window.listen()
window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")

# 장애물
obstacles = []
num_of_obstacles = 5
obstacle_speed = 3

# 버킷 모양 정의
window.register_shape("bucket_hat", ((-25, 30), (-25, 10), (-20, 10), (-20, -30), (0, -30), (0, 10), (25, 10), (25, 30)))

for _ in range(num_of_obstacles):
    obstacle = turtle.Turtle()
    obstacle.speed(0)
    obstacle.shape("bucket_hat")  # 버킷햇 모양으로 설정
    obstacle.color("black")  # 검은색으로 변경
    obstacle.penup()
    x = random.randint(300, 600)
    y = random.randint(-280, 280)
    obstacle.goto(x, y)
    obstacle.setheading(random.randint(0, 360))
    obstacles.append(obstacle)

# 점수
score = 0

# 점수 표시
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("black")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(-380, 260)
score_pen.write("점수: {}".format(score), align="left", font=("Courier", 24, "normal"))

# 게임 루프
while True:
    window.update()

    # 장애물 이동
    for obstacle in obstacles:
        x = obstacle.xcor()
        y = obstacle.ycor()
        x -= obstacle_speed
        obstacle.setx(x)

        # 장애물이 화면 밖으로 나갔을 때
        if obstacle.xcor() < -380:
            x = random.randint(300, 600)
            y = random.randint(-280, 280)
            obstacle.goto(x, y)
            obstacle.setheading(random.randint(0, 360)) 

            # 점수 증가
            score += 10
            score_pen.clear()
            score_pen.write("점수: {}".format(score), align="left", font=("Courier", 24, "normal"))

            # 난이도 증가
            if score % 200 == 0:
                num_of_obstacles += 1
                obstacle_speed += 1

                obstacle.setheading(obstacle.heading() + 5)

        # 플레이어와 장애물 충돌 체크
        if player.distance(obstacle) < 20:
            # 게임 오버 시 재시작 여부 묻기
            answer = messagebox.askyesno("게임 오버", "당신은 엄준식이 되었습니다!!")
            if answer:
                player.goto(-350, 0)
                for obstacle in obstacles:
                    x = random.randint(300, 600)
                    y = random.randint(-280, 280)
                    obstacle.goto(x, y)
                score = 0
                num_of_obstacles = 5
                obstacle_speed = 3
                score_pen.clear()
                score_pen.write("점수: {}".format(score), align="left", font=("Courier", 24, "normal"))
            else:
                window.bye()
                break

turtle.done()
