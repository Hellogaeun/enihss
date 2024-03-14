a = 100
print(type(a))



"""a,b = map(int,input("두 개의 정수를 입력하세요 :").split())
if a%b == 0:
    print("{0:d}은(는) {1:d}의 배수입니다.".format(a,b))"""

#d는 정수를 쓰라는 뜻 !


"""n = int(input(" 연도를 입력하세요 :"))
if (n%4 ==0) and (n%100 !=0) or (n%400 == 0):
    print(n,"은 윤년입니다.")"""

#변수는 ""안에 들어갈 수 x

"""total = 0
numbers = [10, 20, 30, 40, 50]
for m in numbers:
    total = total + m
print(total)"""

#range범위 : 항상 0부터 시작 !

"""total = 0
for i in range(10):
    total = total + i
print(total)

total = 0
i = 0
while True:
    total += i
    i += 1
    if(i>=10) :break 
print(total)"""

"""total = 0
i = 0
while i<10:
    if i%3 ==0:
        i+=1
        continue
    total += i
    i += 1
print(total)"""

"""total = 0
i = 0
while i<10:
    i+=1
    if i%3==0:continue
    total=+i
print(total)"""

#3의 배수면 아래를 진행하지말고 다시 돌아가라는 의미로 continue 사용
#for문 안에 for문 또 들어갈 수 있음 : 2중 roof
#3장 연습문제 홀수번 풀어오기 .............ㅠㅠ
