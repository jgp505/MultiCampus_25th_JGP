import pandas as pd

# 문제 0
df = pd.read_csv("종합연습문제1수정3.csv",encoding='cp949')
print(df.iloc[0,0])

def printStr(num) :
    print(df.iloc[num,0],end='\t')

# 문제 1
printStr(1)
sum1 = 0
for i in range(1,10001) :
    sum1 += i
print(sum1)

# 문제 2
printStr(2)
def myAdder() :
    sum1 = 0
    for i in range(1, 10001):
        sum1 += i
    return sum1
sum1 = myAdder()
print(sum1)

# 문제 3
printStr(3)
def myAdder2(x,y) :
    sum1 = 0
    for i in range(x,y+1) :
        sum1 += i
    return sum1
print(myAdder2(1,10000))

# 문제 4
printStr(4)
myList=[1,7,5,3,2,0,8,9,11,250,320,640]
data = pd.Series(myList)
print()
print(data.describe())
print("총 합 : ", data.sum())

#문제 5,6
printStr(5)
article = df.iloc[5,1]
def myCount(string,word) :
    return string.count(word)

print("\n",myCount(article, "인공지능"))

# 문제 7
keyWord = ['인공지능','AI','GPT']
for k in keyWord :
    print(k,myCount(article,k))

# 문제 8
def writeFile(title,list1) :
    with open(title,'w',encoding='utf-8') as fi :
        for i in list1 :
            fi.write(i)

myDict = {'첫번째':'1번째','두번째':'2번째','세번째':'3번째'}
f = open("test.txt",'r',encoding='utf-8')

i = 0 ; new_text = []
while True :
    text = f.readline()

    if not text :
        f.close()
        break
    elif i < 3 :
        words = text.split()
        text.replace(words[1],myDict[words[1]])
    new_text.append(text)
    i += 1

########################################################################
# 함수 생성(선언)
########################################################################
def fileReader(filename):
    with open(filename, 'rt', encoding='utf-8') as f:
        text = f.readlines()
    return text

def fileWriter(filename, newText):
    with open(filename, 'wt', encoding='utf-8') as f:
        for line in newText:
            # 문자열 맨뒤에 줄바꿈 문자 추가
            f.write(line+'\n')

def replaceStr(text):
    myDict ={'첫번째':'1번째','두번째':'2번째','세번째':'3번째'}
    newText=[]
    i = 0

    while True:
        if i<3:
            # 읽어온 한 줄의 문자열에 줄바꿈이 있으면 삭제
            text[i] = text[i].replace("\n", "")
        else:
            break

        # 하나의 문자열을 공백 기준으로 나눠주는 함수
        words = text[i].split()

        # 마지막 줄이 아니라면
        if i<3:
            # myDict의 key와 value를 참조하여 단어 대체하기
            for key,value in myDict.items():
                if key==words[1]:
                    # 3. 문자열을 다른 단어로 대체하기
                    temp = text[i].replace(key, value)
                    #print("replace이전:{}".format(text[i]))
                    #print("replace이후:{}".format(temp))
                    newText.append(temp)
        else:
            newText.append(text)

        i+=1

    return newText


########################################################################
# 함수 호출 및 실행
########################################################################
text = fileReader(readFile)
newText = replaceStr(text)
print(newText)
fileWriter(writeFile, newText)

print(new_text)
'''
for e1,i in enumerate(text) :
    string = ''
    if e1 < 3 :
        for e2,j in enumerate(i.split()) :
            if e2 == 1 :
                string += "%i번째"%(e1+1)
            else :
                string += j
            string += " "
        string += "\n"
    else :
        string = i
    new_text.append(string)
writeFile("test_2.txt",new_text)
'''
#문제 9
text = open("news.txt",'r',encoding='utf-8').readlines()
new_text = []
for i in text :
    new_text.append(i.replace("인공지능","AI"))
writeFile("news_2.txt",new_text)