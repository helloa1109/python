"""
파이썬에서 함수(모듈,메서드) 선언하는 방법
def 함수명([인수]):
    코드1
    코드2
    [return 값]
"""

def func1():
    print("함수호출!!")

#func1() 함수호출
func1()
func1()

#숫자를 인자로 받아서 1부터 그 숫자까지 출력하는 함수
def numout(n):
    for i in range(1,n+1):
        print(i,end="")
    print()

#numout 함수호출
numout(10)
numout(5)

#숫자를 인자로 받아서 1부터 그 숫자까지 합을 반환하는 함수
def numsum(n):
    sum = 0
    for i in range(1,n+1):
        sum+=i
    return sum

#numsum 함수호출
n1 = numsum(10)
print(n1)

n2 = numsum(500)
print(n2)