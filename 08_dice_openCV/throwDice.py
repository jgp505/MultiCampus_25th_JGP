import cv2
import numpy as np
import matplotlib.pyplot as plt
img1 = cv2.imread("data/dice1.jpg")
img2 = cv2.imread("data/dice2.jpg")
img3 = cv2.imread("Ddata/dice3.jpg")
img4 = cv2.imread("data/dice4.jpg")
img5 = cv2.imread("data/dice5.jpg")
img6 = cv2.imread("data/dice6.jpg")

imgList = [img1, img2, img3, img4, img5, img6]

while True :
    diceNumList = np.random.randint(0, 6,size=3)
    if diceNumList.sum() == 7:
        for e,name in enumerate(['1st','2nd','3rd']) :
            cv2.imshow(name,imgList[diceNumList[e]])

    # 일정시간 키입력을 기다리는 함수 이지만, 0인 경우 키 입력이 들어올때까지 대기
    key = cv2.waitKey(0)

    if key == ord('x') :
        break

cv2.destroyAllWindows()
