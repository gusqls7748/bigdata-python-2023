#CSV 파일 읽기
import csv

# \ufeff가 숨어있을 이경우 encoding='utf-8-sig'로 변경
# csvfile='부산광역시_시내버스_이용건수.csv'
csvfile='충청북도_푸드뱅크현황.csv'
dirname='./Day03/csv/'# ./Day03 뒤에 /붙이는거랑 아닌거랑 먼 차이지

fr = open(f'{dirname}{csvfile}',mode='rt', encoding='utf-8') # 한국어는 기본이 cp949 -> 엑셀에서(utf-8방식) 다른이름으로 저장
reader = csv.reader(fr, delimiter=',') # delimite(구분자)가 ,일 경우

for line in reader:
    print(line)

fr.close()