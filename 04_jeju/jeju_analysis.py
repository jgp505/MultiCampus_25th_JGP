import pandas as pd
import folium
from geopy.geocoders import Nominatim
from collections import defaultdict

# 전처리 과정
def PreProcess(path) :
    # 01. 파일 불러오기
    df = pd.read_csv(path, encoding='cp949')
    df.drop(['허가일자','구분','데이터기준일자'],axis=1,inplace=True)
    # 02. 태양광 선별
    ndf = df[df['원동력종류'] == '태양광']

    # 03~05. 사업 개시일 to datetime 으로 변환 후, 정렬 및 index 초기화
    ndf['사업개시일'] = pd.to_datetime(ndf['사업개시일'])
    ndf.sort_values(by='사업개시일', ascending=True, inplace=True)
    ndf.reset_index(drop=True, inplace=True)

    # 06. 위치 column 추가
    ndf['위치'] = ndf['설치행정시'] + ' ' + df['설치지역']
    return ndf

# 경도, 위도 찍어내기
def addrToGeoPos(dataframe) :
    new_dataframe = defaultdict(list)
    geolocoder = Nominatim(user_agent='South Korea', timeout=None)

    for address in dataframe['위치'].unique() :

        if address == '제주시 삼도이동' :
            address = '7, Gija-gil, Jeju-si'
        else :
            address = "제주특별자치도 %s" % (address.split()[-1])
            #address = address.replace("시","")

        geo = geolocoder.geocode(address)
        new_dataframe['위치'].append(address)
        if geo == None :
            new_dataframe['위도'].append(0)
            new_dataframe['경도'].append(0)
        else :
            new_dataframe['위도'].append(geo.latitude)
            new_dataframe['경도'].append(geo.longitude)

    ndf = pd.DataFrame(new_dataframe).set_index("위치")
    return ndf

path = "제주특별자치도_신재생에너지발전시설현황_20200120.csv"

# 그림 그리기
def drawMarker(df_unique) :
    korea_map = folium.Map(location=[33.38, 126.55], zoom_start=11)
    for i in range(len(df_unique)) :
        folium.Marker([df_unique.iloc[i][0], df_unique.iloc[i][1]],
                      popup=df_unique.index[i]).add_to(korea_map)
    return korea_map

# 전처리 과정
df = PreProcess(path)
print(df.info())

# 경도, 위도 데이터 뽑기
ndf = addrToGeoPos(df)

# 데이터 뽑기
drawMarker(ndf).save("jeju_solar.html")