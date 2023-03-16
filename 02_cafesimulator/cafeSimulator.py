# 카페에서 주문을 받고 제품을 내주는 과정을 시뮬레이션하고, log.txt 파일로 기록을 남기는 프로그램
import time
import random

# 1. 메뉴를 출력
# 아메리카노, 라떼, 바닐라라떼, 녹차라떼, 콜드브루

def printMenu() :
    print("="*20)
    print("1. 아메리카노  \\2500")
    print("2. 라떼  \\3000")
    print("3. 바닐라라떼 \\3500")
    print("4. 녹차라떼 \\3500")
    print("5. 콜드브루 \\2700")
    print("="*20)

def autoKey() :
    num = random.randint(1,8)
    if num == 7 :
        num = 'exit'
    return num

# 2. 주문을 받음
# input()함수를 사용해서 키보드 입력으로 주문을 받음

def inputKey(num) :
    opened = True
    #rawInput = input("주문하시겠습니까? >> ")
    rawInput = num
    # 과제 : 만약 숫자가 아닌 입력 문자열이 들어온 경우, 어떻게 걸러낼것인가?
    if rawInput != 'exit' :
        inputMenu = int(rawInput)
    else :
        opened = False
        inputMenu = None
    return opened, inputMenu

# 3. 음료를 만드는데 시간
# sleep() 함수를 통해서 만드는 시간 모델링
# 아메리카노 1초, 라떼 2초, 바닐라라떼 3초, 녹차라떼 3초, 콜드브루 1초

def makeCoffee(menuNum) :

    if menuNum == 1 :
        time.sleep(1)
        string = "아메리카노" ; price = 2500
    elif menuNum == 2 :
        time.sleep(2)
        string = "라떼" ; price = 3000
    elif menuNum == 3:
        time.sleep(3)
        string = "바닐라라떼" ; price = 3500
    elif menuNum == 4 :
        time.sleep(3)
        string = "녹차라떼" ; price = 3500
    elif menuNum == 5:
        time.sleep(1)
        string = "콜드브루"; price = 2700
    return string, price

# 4. 음료가 만들어지면 log.txt파일에 남긴다.
def newLog() :
    f = open("log.txt", 'w')
    f.close()

def writeLog(makedCoffee, totalPrice) :
    with open("log.txt", 'a', encoding='utf8') as fi:
        fi.write(f"[{time.strftime('%H:%M:%S')}]주문하신 {makedCoffee}가 완성되었습니다.\t")
        fi.write(f"현재 가격 : {totalPrice}\n")
    fi.close()

totalPrice = 0
newLog()
while True :
    # 1. 메뉴를 출력
    printMenu()

    # 2. 주문을 받음
    nums = autoKey()
    opened, inputMenu = inputKey(nums)

    if not opened :
        print("주문된 총 가격은 \\%i 입니다." % (totalPrice))
        break
    else :
        if inputMenu < 1 or inputMenu > 5 :
            print("Menu에 존재하지 않는 메뉴입니다. 다시 주문해주세요.")
        else:
            # 3. 음료를 만드는데 시간
            coffee, price = makeCoffee(inputMenu)
            totalPrice += price
            # 4. 음료가 만들어지면 log.txt파일에 남긴다.
            writeLog(coffee, totalPrice)
            print("%s 주문이 완료되었습니다. 현재 가격 : \\ %i" % (coffee, totalPrice))