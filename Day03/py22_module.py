# 모듈 사용
# import datetime as dt -> 모든걸 다가지고 오는것

from datetime import datetime # as dt, 필요한것만 가지고 와서 사용할 수 있다.
from os import getcwd # 함수만 가져올 수 도있다

curr_date = datetime.now() # = dt.now() = #dt.datetime.now()
print(curr_date)
print(getcwd())