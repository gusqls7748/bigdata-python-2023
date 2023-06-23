# 다중 입력

# 얘는 튜플의 형태
# map으로 형변환
(x, y) = map(int, input('두개 수를 입력하세요(구분자 ,) > ').split(',')) 

print(type(x))
print(type(y))
print(x + y)

# 출력할때
# Escape char \n \t \b \' \" == java와 동일
# formatting %d,.4f... == java와 동일 