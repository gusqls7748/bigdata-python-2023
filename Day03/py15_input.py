# 입출력
import datetime # 날짜 모듈 가져옴

birth_year = int(input('출생년도를 입력하세요 > ')) # 키보드 입력(무저건 String)

print(f'당신의 출생년도는 {birth_year}년 입니다.') # 콘솔출력
curr_year = datetime.datetime.now().year # yyyy-MM-dd hh:mm:ss.ms
# print(curr_year)

# input은 String이기 때문에 연산을 위해 birth_yea를 int()로 형변환을 해주면 숫자로 인식되어 계산한다.
age =curr_year - birth_year
print(f'당신의 나이는 {age}세 입니다')

a=123
a= [3, 6, 9]
print(a)

print('Life' 'is' 'short')
print('Life' + 'is' + 'short') # 위와 동일
print('Life', 'is', 'short') # 좀 더 일반적, 공백이 생긴다

print('Life' '3.141592' 'True')
print('Life', '3.141592', 'True')

print(range(10))
print(len(range(10)))

for i in range(10):
    if i == (len(range(10))-1):
        print(i,end='\n') # 엔터를 없앨때 (기본은 밑으로 나열되는데, 옆으로 나열되게 함)
    else:
        print(i,end=', ')

print('Life', 'is', 'short', sep='&') # 별로 안쓰임

pi = 3.14159265359

print(f'PI= {pi:.4f}') # format string
print(f'PI= {pi:20.2f}') # 앞에 공백을 주는 format string