#coding:utf8
import MySQLdb
import random
myCon = MySQLdb.connect(host='localhost', passwd='badperson3', db='UserRank', user='root', charset='utf8')
#总共100个用户
for i in xrange(100, 200):
    sql = 'insert into UserRank (uid, score) values(%d, %d)' % (i, random.randint(0, 100))
    myCon.query(sql)

myCon.commit()
myCon.close()
