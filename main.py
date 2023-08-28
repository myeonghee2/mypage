import random

random_number = random.randint(1, 100)

count = 0

while True:
    try:
        count += 1
        number= int(input("숫자를 입력하세요:"))     
        if number == random_number:
            print(f"정답! {count}번 만에 정답을 맞췄습니다.")
            print("재시작 하시겠습니까? y/n")
            replay = input("")
            if replay == "n":
                print("종료합니다.")
                break
            elif replay == "y":
                print("재시작합니다.")
                count = 0
                random_number = random.randint(1, 100)                
            else:
                print("y/n 중 입력해주세요.")
                print("재시작 하시겠습니까? y/n")
        elif (number > random_number and number<100):
            print("다운")
        elif (number < random_number and number<100):
            print("업")
        else: 
            print("1~100까지의 숫자만 입력이 가능합니다.")
    except:
        print("1~100까지의 숫자만 입력이 가능합니다.")


 