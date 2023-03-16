from datetime import datetime
import pymysql

class PythonSQL :
    def __init__(self,host='127.0.0.1',password='0000',
              dbname='soloDB',tablename='new_table'):
        self.host = host
        self.password = password
        self.db = dbname
        self.table = tablename
        self.conn = pymysql.connect(host=self.host,user='root',
                                    password=self.password,db=self.db,
                                    charset='utf8')
           
    def inputData(self):
        data1 = input("사용자 ID ==> ")
        data2 = input("사용자 이름 ==> ")
        data3 = input("사용자 이메일 ==> ")
        data4 = input("사용자 출생연도 ==> ")
        #birthday = datetime.strptime(data4, "%Y-%m-%d")
        #data4 = "{0:4d}-{1:02d}-{2:02d}".format(birthday.year, birthday.month, birthday.day)
        return (data1, data2, data3, data4)

    def storeDB(self,datas=False):
        if datas :
            data1,data2,data3,data4 = datas
        else :
            data1,data2,data3,data4 = self.inputData()
        sql = "INSERT INTO %s VALUES (%d, '%s', '%s', %d)" % (self.table,int(data1), data2, data3, int(data4))
        self.conn.cursor().execute(sql)
        self.conn.commit()
        self.conn.close()

    def readDB(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM %s"%(self.table))

        print("사용자ID    사용자이름    이메일        출생연도")
        print("----------------------------------------------------")
        while True :
            row = cursor.fetchone()
            if row == None :
                break

            data1,data2,data3,data4 = row
            print("%5s   %15s   %20s   %d" % (data1, data2, data3, int(data4)))
        self.conn.close()
        
if __name__ == '__main__' : 
    
    # 데이터 베이스 생성
    conn = pymysql.connect(host='127.0.0.1',user='root',password='0000',
                            charset='utf8')
    try :
        with conn.cursor() as cursor : 
            sql = 'CREATE DATABASE test'
            cursor.execute(sql)
            conn.commit()
    except :
        pass
    conn.close()
   
   # 테이블 생성
    conn = pymysql.connect(host='127.0.0.1',user='root',password='0000',
                            charset='utf8',db='test')
    try :
        with conn.cursor() as cursor :
            sql = '''
            CREATE TABLE userTable (
            userID int(4) NOT NULL PRIMARY KEY,
            userName char(15) NOT NULL,
            email char(20),
            birthYear int(4))
            '''
            cursor.execute(sql)
        conn.commit()
    except :
        pass
    conn.close()
    
    # 테이블에 데이터 넣기
    '''
    load_sql = PythonSQL(password='0000',dbname='test',tablename='userTable')
    while True :
        #datas = ('1','이병헌','Lee@naver.com','1996')
        datas = load_sql.inputData()
        if datas[0] == '' :
            break
        load_sql.storeDB(datas=datas)
    '''   
    
    # 테이블 데이터 살펴보기
    load_sql = PythonSQL(password='0000',dbname='test',tablename='userTable')
    load_sql.readDB()
    