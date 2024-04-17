#9,1

num1 = Add(133)
num2 = Add(334)
result = num1 + num2
print(result)

num1 = mul(133)
num2 = mul(334)
result1 = num1 + num2
print(result1)

num1 = sub(133)
num2 = sub(334)
result2 = num1 - num2
print(result2)

a = truediv(123)
b = truediv(3)
result3 = a/b
print(result3)



#9.3

s = 'Hello world~'
sorted(s)
print(s)
print(s.upper())


#9.5

class check:
    a = 1
    b = 1
    c = 2
    d = 3
    e = 3
    def __init__(self,num):
        self.num=num
    def c1(self,other):
        if self.num==other.num:
            return True
        else:
            return False

check1=check(check.a)
check2=check(check.b)
cehch3=check1.c1(check2)
print(chech3)
