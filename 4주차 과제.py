#4.1

def my_greet():
    print('환영합니다.')

my_greet()
my_greet()


#4.3

def max2(m,n):
    if :
        return
    else:
        return

def min2(m,n):
    if :
        return
    else:
        return

print('100과 200중 큰 수는 :', )
print('100과 200중 작은 수는 :', )




#4.9

nums =list(map(float,input('정수를 여러 개 입력하시오:').split()))

def mean_of_n(nums):
    total=0
    for num in nums:
        total=total+num
    mean= total/len(nums)
    return mean

def max_of_n(nums):
    max=nums[0]
    for num in nums:
        if num>max:
            max=num
        return max

def min_of_n(nums):
    min=nums[0]
    for num in nums:
        if num<min:
            min = num
        return min

print('평균값은',mean_of_n(nums))
print('최댓값은',max_of_n(nums))
print('최솟값은',min_of_n(nums))
