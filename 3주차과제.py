#3.1


#3.3
"""x = int(input("나이를 입력하시오 :"))
y = int(input("키를 입력하시오(단위 cm) :"))
if x>=19 and y>=150 :
    print("입장할 수 있습니다.")"""


#3.5
"""a,b = map(int,input("두 정수를 입력하시오 :").split())
if a>b :
    print("{0:d},{1:d}".format(a,b))
else :
    print("{0:d},{1:d}".format(b,a))"""


#3.7
"""x = int(input("게임점수를 입력하시오 :"))
if x>=1000 :
    print("고수입니다.")
else :
    print("입문자입니다.")"""


#3.9
"""x = int(input("정수를 입력하시오 :"))
if x%2==0 :
    print(x,"는(은) 2(으)로 나누어집니다.")
if x%2!=0 :
    print(x,"는(은) 2(으)로 나누어지지 않습니다.") 
if x%3==0 :
    print(x,"는(은) 3(으)로 나누어집니다.")
if x%3!=0 :
    print(x,"는(은) 3(으)로 나누어지지 않습니다.") 
if x%2==0 and x%3==0 :
    print(x,"는(은) 2와(과) 3 모두로 나누어집니다.")
else :
    print(x,"는(은) 2와(과) 3 모두로 나누어지지 않습니다.")"""


#3.11
"""a,b,c = map(int,input("세 복권번호를 입력하시오 :").split())
if a == 2 and b == 3 and c == 9 :
    print("상금 1억 원")
elif a == 2 and b == 3 and c !=9 :
    print("상금 1천만 원")
elif a ==2 and b !=3 and c == 9 :
    print("상금 1천만 원")
elif a !=2 and b==3 and c==9 :
    print("상금 1천만 원")
elif a !=2 and b!=3 and c==9 :
    print("상금 1만 원")
elif a !=2 and b ==3 and c!=9 :
    print("상금 1만 원")
elif a==2 and b!=3 and c!=0 :
    print("상금 1만 원")
else :
    print("다음 기회에...")"""


#3.13
"""x,y = map(int,input("점의 좌표 x,y를 입력하시오 :").split())
z = ((x-3)**2 + (y-4)**2)**1/2
if z>10 :
    print("점이 외부에 있음")
else :
    print("점이 내부에 있음")"""


#3.15-(for)
"""total = 0
for i in range(1,10):
    total=2*i
    print("2 *",i,"=", total)"""


#3.15-(while)
"""total = 0
i = 1
while i<10 :
    total=2*i
    print("2 *",i,"=", total)
    i += 1"""


#3.17(1)
"""for i in range(3):
    print('python')
    print('is')
    print('FUN!')"""


#3.17(2)
"""for i in range(3):
    print('python')
    print('is.')
print('FUN!')"""


#3.17(3)
"""for i in range(3):
    print('python')
print('is')
print('FUN!')"""


#3.19 

"""print("맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.")

print("-햄버거(입력b)")
print("-치킨(입력c)")
print("-피자(입력p)")

x = input("메뉴를 선택하세요(알파벳 b,c,p 입력) :")
#int = 숫자를 집어넣을때 만약 문자면 바로 인풋 ㅇㅋ?

b ="b"
c ="c"
p ="p"

if x ==b :
    print("햄버거를 선택하였습니다.")
elif x ==c :
    print("치킨을 선택하였습니다.")
elif x ==p :
    print("피자를 선택하였습니다.")
else :
    print("메뉴를 다시 입력하세요(알파벳 b,c,p 입력) :")"""


#3.21 --- 다시 실시한다 실시

"""n = int(input("숫자를 입력하세요 :"))"""

    
#3.23

"""n = int(input("숫자를 입력하세요 :"))
iend = n
total = 0
for i in range(1,iend+1) :
    total = total + i**2
print("결과는", total, "입니다.")"""


#3.25

"""snail = 0
x = 0

while snail<30 :
    x = x+1
    snail = snail + 7
    print("day :",x, "달팽이의 위치 :", snail,"m")
    if snail <30 :
        snail = snail - 5
print("우물을 탈출하는 데 걸린 날은", x, "일 입니다.")"""


#3.27

"""print("세 자리의 암스트롱 수 :",end=" ")

for i in range(100,1000,1):
    a1 = int(str(i)[0])
    a2 = int(str(i)[1])
    a3 = int(str(i)[2])
    result = (a1**3) + (a2**3) + (a3**3)
    if i == result:
        print(i, end=" ")"""


#3.29

"""fuel = 500
remain = 50

while remain>=10:
    x = int(input("충전 또는 사용한 연료를 +/- 기호와 함께 입력하시오 :"))
    fuel = fuel + x
    remain = fuel / 10
    if remain>=10:
        print("현재 탱크양은", fuel, "입니다.")
    else:
        print("현재 탱크양은", fuel, "입니다.")
        print("경고 : 연료가 10% 미만이니 충전하세요!")
        break"""


#3.31 - 친화수 일단 몰라잉 ~
