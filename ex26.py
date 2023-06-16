import turtle
import random

# 거북이 객체 생성
t = turtle.Turtle()

# 색상 리스트
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "gray", "black"]

# 초기 위치 설정
t.penup()
t.goto(0, 0)
t.pendown()

# 이동 함수 정의
def move_up():
    t.color(random.choice(colors))  # 랜덤 색상 선택
    t.setheading(90)  # 위쪽으로 이동
    t.forward(10)

def move_down():
    t.color(random.choice(colors))
    t.setheading(270)  # 아래쪽으로 이동
    t.forward(10)

def move_left():
    t.color(random.choice(colors))
    t.setheading(180)  # 왼쪽으로 이동
    t.forward(10)

def move_right():
    t.color(random.choice(colors))
    t.setheading(0)  # 오른쪽으로 이동
    t.forward(10)

def reset_position():
    t.penup()
    t.goto(0, 0)  # 초기 위치로 이동
    t.pendown()

# 키 이벤트 처리
turtle.listen()
turtle.onkey(move_up, "Up")  # 위쪽 방향키
turtle.onkey(move_down, "Down")  # 아래쪽 방향키
turtle.onkey(move_left, "Left")  # 왼쪽 방향키
turtle.onkey(move_right, "Right")  # 오른쪽 방향키
turtle.onkey(reset_position, "space")  # 스페이스바

# 메인 이벤트 루프
turtle.mainloop()
