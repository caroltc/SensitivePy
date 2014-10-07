#-*- coding:utf-8 -*-
#localhost testing
#caroltc 2014/10/7
from bottle import route, run, request
from smallgfw import *
import json
import sys

def initWords():
    path = 'words.txt'  
    fp = open(path,'r')  
    word_list = []  
    for line in fp:  
        line = line[0:-1]  
        word_list.append(line)  
    fp.close()
    return word_list

@route('/replace', method="POST")
def replace():
    reload(sys)
    sys.setdefaultencoding('utf8')
    getwords = request.params.words or ""
    gfw = GFW()
    words = initWords()
    gfw.set(words)#设置敏感词列表
    res = gfw.check(getwords.encode('utf8'))
#    for obj in res:
#        print json.dumps(obj),obj[2]
    s = gfw.replace(getwords.encode('utf8'),"**")
    return s

@route('/check',method="POST")
def check():
    reload(sys)
    sys.setdefaultencoding('utf8')
    getwords = request.params.words or ""
    gfw = GFW()
    words = initWords()
    gfw.set(words)#设置敏感词列表
    res = gfw.check(getwords.encode('utf8'))
    resp = {}
    resp['count'] = len(res)
    resp['datas']= res
    return json.dumps(resp)

@route('/test')
def test():
    reload(sys)
    sys.setdefaultencoding('utf8')
    webdata = '<h1>check</h1><form action="/replace" method="post"><input type="text" name="words" /><input type="submit"></from>'
    return webdata


run(host='localhost', port=80, debug=True)