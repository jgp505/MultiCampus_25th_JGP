# 1. input으로 키 입력 받기
#myStr = input("단어를 입력해주세요 >> ")
import pandas as pd
# 2. is_palindrome() 함수 만들기
#def is_palindrome(word) :
#    return word == word[::-1] # 단어를 뒤집었을 때와 안 뒤집었을 때가 같냐

def is_palindrome() :
    e = -1
    for j in range(len(df['text'])//2) :
        if word[j] != word[e] :
            return 0
        e-=1
    return 1

df = pd.read_csv("palindrome.csv",encoding='cp949')
# 3. 실행해서 확인
df['label'] = df['text'].apply(is_palindrome())
print(df)