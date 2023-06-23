# Q2
def avg_numbers(*args): # 값 여러개 받을때  args = tuple
    result = 0
    for i in args:
        result += i
        
    return print(result/len(args))

avg_numbers(1,2) # 1.5 출력
avg_numbers(1,2,3,4,5) # 3.0출력


# Q6
user_input = input("저장할 내용을 입력하세요: > ")
f = open('./Day03/test.txt', mode='a',encoding='utf-8')
f.write(user_input)
# (,end='') -> print에서만 가능한거네
f.write('\n')

f.close()