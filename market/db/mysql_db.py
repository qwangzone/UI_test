import pymysql

class DB(object):

    def delete_user(self):
        self.con = pymysql.connect(host='192.168.3.105', user='root', password='123456', port=3307, db='apd_biz_sina')
        cursor = self.con.cursor()
        cursor.execute("delete from user where mobile = '123****8915'")
        self.con.commit()

    def close(self):
        self.con.close()

if __name__ == '__main__':
    db = DB()
    db.delete_user()
    db.close()



