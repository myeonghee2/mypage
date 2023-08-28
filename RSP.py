import random

select = ["가위", "바위", "보"]
computer = random.choice(select)

comcount = 0
usercount = 0
count = 0
tiecount = 0

while True:
    user= (input("가위바위보!:"))
    if user=="가위" or user=="바위" or user=="보":
        count += 1
        computer = random.choice(select)
        if user == computer:
            print("무승부!")
            tiecount += 1
        elif (user == '바위' and computer=='가위')or(user=='가위'and computer=='보')or(user=="보" and computer=="주먹"):
            print("user가 승리하였습니다!")
            usercount += 1
        else:
            print("computer가 승리하였습니다!")
            comcount += 1

        print(f"user는 {user}를, computer는 {computer}를 냈습니다.")
        print("게임 초기화를 원할 경우 re를 입력해주세요.")

    elif user=="re":
        print("재시작하시겠습니까? y/n")
        re= input("")
        if re == "y":
            print(f"{count}전, {usercount}승, {comcount}패, {tiecount}무승부입니다.")
            print("재시작합니다.")
            comcount, usercount, count, tiecount = (0,)*4
            # usercount = 0
            # count = 0
            # tiecount = 0
            # computer = random.choice(select)
        elif re == "n":
            print("게임을 종료합니다.")
            print(f"{count}전, {usercount}승, {comcount}패, {tiecount}무승부입니다.")
            break
        else:
            print("y/n 중 입력해주세요.")
            print("재시작 하시겠습니까? y/n") 
    else:
        print("가위, 바위, 보 중 입력해주세요.")
