#coding:utf8
#根据用户得分表 初始化用户排名表
import MySQLdb
myCon = MySQLdb.connect(host='localhost', passwd='badperson3', db='UserRank', user='root', charset='utf8')

#删除旧的计数
sql = 'delete from UserCount'
myCon.query(sql)
myCon.commit()


sql = 'select * from UserRank'
myCon.query(sql)
users = myCon.store_result().fetch_row(0, 1)
for i in users:
    sql = 'insert UserCount (`score`, `count`) values (%d, 1) on duplicate key update count = count+1 ' % (i['score'])
    myCon.query(sql)
    
myCon.commit()
myCon.close()


