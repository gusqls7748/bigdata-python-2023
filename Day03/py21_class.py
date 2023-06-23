class Calculator:
    # 무조건 self를 넣어줘야한다(= 나에게 속해있는 함수임을 표시)
    # 밑에 있는 self.result는 다 똑같은 변수
    def __init__(self) -> None: # 생성자는 __이름__로 만듬
        self.result = 0

    def add(self,num):
        self.result += num
        return self.result
    
    
    def sub(self,num):
        self.result -= num
        return self.result
    
mycalc = Calculator() # java와 달리 new 없음, 그냥 ()만 쳐줌/ 만들었던 Calculator() 클래스를 사용 => 안에 있는 함수들을 사용
print(mycalc.add(40))
print(mycalc.add(50))
print(mycalc.sub(50))

val = 10
if val != 10:
    pass # 안쪽에 들어갈 내용을 모르겠을 때 일단 pass로 빨간줄(오류무시)하고 실행 가능