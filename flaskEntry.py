#coding:utf8
import UserRank
import json
from flask import Flask
from flask import _app_ctx_stack
from flask import request

import MySQLdb

DATABASE = 'UserRank'
PASSWORD = 'badperson3'
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)


def get_db():
    top = _app_ctx_stack.top
    if not hasattr(top, 'dbConnect'):
        myCon = MySQLdb.connect(host='localhost', passwd=app.config['PASSWORD'], db=app.config['DATABASE'], user='root', charset='utf8')
        top.dbConnect = myCon
    return top.dbConnect


@app.teardown_appcontext
def closeConnect(exception):
    top = _app_ctx_stack.top
    if hasattr(top, 'dbConnect'):
        top.dbConnect.close()

@app.route("/updateScore")
def updateScore(): 
    myCon = get_db();
    uid = int(request.args['uid'])
    newScore = int(request.args['newScore'])
    UserRank.updateScore(myCon, uid, newScore)
    return json.dumps(dict(id=1))

@app.route('/getRank')
def getRank():
    myCon = get_db();
    score = int(request.args['score'])
    rank = UserRank.getRank(myCon, score)
    return json.dumps(dict(rank=rank))

@app.route('/getUser')
def getUser():
    myCon = get_db();
    rank = int(request.args['rank'])
    uid = UserRank.getUser(myCon, rank)
    return json.dumps(dict(uid=uid))

@app.route('/getRange')
def getRange():
    myCon = get_db();
    start = int(request.args['start'])
    end = int(request.args['end'])
    allUser = UserRank.getRange(myCon, start, end)
    return json.dumps(dict(allUser=allUser))




if __name__ == '__main__':
    app.run()
