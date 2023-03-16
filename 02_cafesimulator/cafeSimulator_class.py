# 카페에서 주문을 받고 제품을 내주는 과정을 시뮬레이션하고, log.txt 파일로 기록을 남기는 프로그램
import time
import random

class CafeSimulator :
    def __init__ (self, cafeName, cafeOpenTime, cafeCloseTime) :
        self.cafeName = cafeName
        self.cafeOpenTime = cafeOpenTime
        self.cafeCloseTime =cafeCloseTime
        self.menuDict = {1:['아메리카노',2500],2:['라떼',3000],3:['바닐라라떼',3500],4:['녹차라떼',3500],5:['콜드브루',2700]}
        self.newLog()

    def printInfo(self):
        print("카페이름 : {}".format(self.cafeName))
        print("카페시작시간 : {}".format(self.cafeOpenTime))
        print("카페마감시간 : {}".format(self.cafeCloseTime))

    def getInfo(self):
        return self.cafeName , self.cafeOpenTime, self.cafeCloseTime

    def printMenu(self) :
        print("="*20)
        for k,v in self.menuDict.items() :
            print("%i. %s \\%i"%(k, v[0],v[1]))
        print("="*20)

    def autoKey(self) :
        self.menuNum = random.randint(1,7)
        self.price = True

        if self.menuNum >= 6 :
            self.menuNum = 'exit'
            self.price = False
        else :
            self.string = self.menuDict[self.menuNum][0]
            self.price = self.menuDict[self.menuNum][1]
            print("%s를 준비하고 있습니다. 잠시만 기다려주세요."%(self.string))
            if self.menuNum == 1 or self.menuNum == 5:
                time.sleep(1)
            elif self.menuNum == 2 :
                time.sleep(2)
            elif self.menuNum == 3 or self.menuNum == 4 :
                time.sleep(3)

    def newLog(self):
        f = open("log.txt", 'w')
        f.close()

    def writeLog(self,totalPrice) :
        with open("log.txt", 'a', encoding='utf8') as fi:
            fi.write(f"[{time.strftime('%H:%M:%S')}]주문하신 {self.string}가 완성되었습니다.\t")
            fi.write(f"현재 가격 : {totalPrice}\n")
        fi.close()


# 클래스의 객체 생성
cafeName1 = '오늘' ; cafeOpenTime1 = '9:00' ; cafeCloseTime1 = '21:00'
cafeName2 = '내일' ; cafeOpenTime2 = '10:00' ; cafeCloseTime2 = '22:00'

myCafe = CafeSimulator(cafeName1, cafeOpenTime1, cafeCloseTime1)

totalPrice = 0
myCafe.printInfo()

while True :
    # 1. 메뉴 출력
    myCafe.printMenu()

    # 2. 주문 받음
    myCafe.autoKey()
    if not myCafe.price :
        if totalPrice == 0 :
            print("다음에 또 오세요.")
        else :
            print("주문된 총 가격은 \\%i 입니다." % (totalPrice))
        break
    else :
        # 3. 커피 만듬
        totalPrice += myCafe.price

        # 4. log 남기기
        myCafe.writeLog(totalPrice)
        print("%s 주문이 완료되었습니다. 현재 가격 : \\ %i" % (myCafe.string, totalPrice))


