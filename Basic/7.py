# error 처리 : try except 문
try:
    a = 3/0
    print(a)
except Exception as log:
    print("Error :", log)
