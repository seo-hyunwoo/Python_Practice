#첫 명령어는 들여쓰기 없이 시작해야 함. 파이썬은 들여쓰기가 중요함.
#조건문, 반복문 등의 문법을 사용할 때는 콜론: 으로 명령어의 끝을 알림.
#콜론: 의 다음 줄 부터는 들여쓰기의 간격이 모두 일정해야 함.

score = 85

if score < 90 and score >= 80 :
    print("Good")
    print("score")

elif score >= 70 :
    print("Not Bad")

else :
    print("Bad")
print("한글")

list = [1, 2, 3]
if 2 in list :
    print("2가 리스트에 포함되어 있음.")
