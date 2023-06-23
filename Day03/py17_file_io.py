# 파일 입출력
# DB open / close ,  Network open / close , File open / close  => close안해주면 큰 책임 
import os

cur_path = os.getcwd() # 현재 파이썬 경로 (많이 사용)
print(f'파이썬의 현재 절대경로는 {cur_path} 이다.')

filename = './Day03/sample.txt'
# filename = 'C:\\Source\\Pythone_2023\\Day03\\test.txt' # 절대경로 쓸거면 \\ 두번으로 해야 '\b' 같은 이스케이프문자에 안걸리고 정상 경로설정 => 파이썬
# filename = 'C:/Source/Pythone_2023/Day03/test2.txt' # 이제는 거의 통합? 되서 / 로도 경로 설정 가능 => 리눅스, 유니온과 동일

# w(쓰기),r(읽기) 제일 많이씀/ a(append, 추가)도 좀 씀 / wt: 텍스트 모드로 쓰기 
f = open(filename,mode='wt',encoding='utf-8') # 텍스트 파일 생성(ascii 코드 기본) 


f.write('인생은 짧습니다. 파이썬을 쓰세요~\n') # \n 해줘야 한 줄 내려감
f.write('인생은 아름다워 \n')  # 마지막 문장에는 \n 안쓰는게 좋다
f.write('가자!')
f.write('집에!!')

f.close() # 무조건 닫아줘야함  
print(f'{filename} 이(가) 생성되었습니다')

# 파일 읽기
fr = open(filename, mode='r',encoding='utf-8')
while True: # 무한루프
    line = fr.readline() # 한줄씩 읽기
    if not line: break # 읽을 줄이 없으면 빠져나감
    print(line, end='') # \n과 엔터가 두번 들어감 -> 그냥 프린트 하면 한줄 공백이 생기기 때문에 end='' 처리가 필요

fr.close() # 파일 닫기(반드시)

