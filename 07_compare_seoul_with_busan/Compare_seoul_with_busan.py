import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("OBS_ASOS_TIM_20230308150606.csv",encoding='cp949')
df.columns = ['지점','지점명','일시','기온','습도','지면온도']
df['일시'] = pd.to_datetime(df['일시'])
df.drop('지점', axis=1,inplace=True)

#  서울 지점
seoul_df = df.query("지점명 == '서울'")
busan_df = df.query("지점명 == '부산'")

plt.figure(figsize=(8,6))
plt.plot(seoul_df['일시'],seoul_df['기온'],'r-',label='Seoul')
plt.plot(busan_df['일시'],busan_df['기온'],'b-',label='Busan')
plt.legend(frameon=False)
plt.show()