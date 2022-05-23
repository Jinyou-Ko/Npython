Total = 0
Counter = 1
while Counter <= 10:
    grade = int(input("점수를 입력하세요."))
    Total = grade + Total
    Counter = Counter + 1

aver = Total / 10
print(aver)
print(Total)