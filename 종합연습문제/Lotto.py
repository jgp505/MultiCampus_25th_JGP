import numpy as np
# 파이썬 로또 게임 1~45까지 숫자를 선택,
# 내 번호가 있으면(input함수) 내 번호가 몇개가 맞았는지 확인

# 로또 번호 추출기
def lottoNumGen(auto, lottoCount):
    if auto == False:
        # 키보드로 6개의 숫자를 입력 받는다.
        myNumList = ((input("로또 숫자를 입력하세요:").split(',')))
        myNumList = list(map(int, myNumList))
    else:
        myNumList = np.random.choice(45, num, replace=False)
        myNumList = sorted(myNumList)
    return myNumList


def lottoMachine(num):
    # 로또 숫자 추첨기
    numList = np.random.choice(45, num, replace=False)
    numList = sorted(numList)

    return numList


# 로또 숫자 비교기
# 비교해서 결과값까지 다 출력
def lottoCompare(myNumList, numList):
    count = 0
    for myNum in myNumList:
        for num in numList:

            if myNum == num:
                count += 1
                print(myNum, end=' ')

    print(" ")
    print("로또 추첨기와 동일한 숫자의 갯수는:{}".format(count))
    return count
counts = 0
while True :
    DEBUG = True

    # 로또 숫자의 갯수
    num = 6

    ######################################
    # 로또 번호 추출기 호출
    ######################################
    # 자동으로 생성하려면 첫번째 인수에 True
    # 수동으로 입력하려면 첫번째 인수에 False
    myNumList = lottoNumGen(True, num)

    if DEBUG == True:
        print("생성된 로또 번호:{}".format(myNumList))

    ######################################
    # 로또 추첨기 호출
    ######################################
    numList = lottoMachine(num)

    if DEBUG == True:
        print("추첨된 로또 번호:{}".format(numList))

    compare = lottoCompare(myNumList, numList)

    if compare >= 4 :
        print(counts)
        break
    else :
        counts += 1