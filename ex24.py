import random
import turtle as t

# 이동할 거리길이를 입력해서 반환하는 함수(입력을 다이얼로그로 받기)
def inp():
    n = int(t.textinput("이동거리입력","input number"))
    return n

list=["red","pink","orange","green","gray"]
t.shape("turtle")
t.width(3)
t.color("orange")

while True:
    n=inp()
    if n==0:
        print("종료합니다")
        break
    idx=random.randint(0,4)
    t.color(list[idx])
    t.fd(n)
    t.setheading(abs (n))

t.exitonclick()



