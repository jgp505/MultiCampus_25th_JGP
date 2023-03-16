# 1. 이미지가 저장된 폴더 문자열 변수를 생성
srcPath = "D:/MultiCampus/PycharmProject/train/train/"

import os
import glob
import shutil

filenames = os.listdir(srcPath)

# 폴더의 파일 갯수를 확인
print(len(filenames))

dirname1 = srcPath + 'dog'
dirname2 = srcPath + 'cat'
os.makedirs(dirname1, exist_ok=True)
os.makedirs(dirname2, exist_ok=True)

jgpFile = glob.glob(srcPath + '*.jpg')

for filename in jgpFile :
    baseFileName = os.path.basename(filename)
    category,_,_= baseFileName.split(".")
    dst = srcPath + category + '/' + baseFileName
    shutil.copy(filename, dst)