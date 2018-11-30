#!/usr/bin/python
# coding: utf-8

#python实现微信企业号的文本消息推送

import urllib2
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def gettoken(corpid,corpsecret):
    gettoken_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid='+corpid+'&corpsecret='+corpsecret
    try:
        token_file = urllib2.urlopen(gettoken_url)
    except urllib2.HTTPError as e:
        print e.code
        print e.read().decode("utf8")
        sys.exit()
    token_data = token_file.read().decode('utf-8')
    token_json = json.loads(token_data)
    token_json.keys()
    token = token_json['access_token']
    return token
def senddata(access_token,user,party,agent,subject,content):
    send_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token='+access_token
    send_values = "{\"touser\":\"" + user + "\",\"toparty\":\""+party+"\",\"totag\":\"\",\"msgtype\":\"text\",\"agentid\":\""+agent+"\",\"text\":{\"content\":\""+subject+"\n"+content+"\"},\"safe\":\"0\"}"
    send_request = urllib2.Request(send_url,send_values)
    response = json.loads(urllib2.urlopen(send_request).read())
    print str(response)
     
user1='@all'
partyid='@all'
agentid='12345'
subjectText='Reminder'
contentPath='/home/11weixin.txt'
contents=[]
#初始化lie列表
file = open(contentPath)
contents=file.read()

if __name__ == '__main__':
    user = user1  # 参数1:发送给用户的账号,必须关注企业号,并对企业号有发消息权限
    party = partyid  # 参数2:发送给组的id号,必须对企业号有权限
    agent = agentid  # 参数3:企业号中的应用id
    subject = subjectText  # 参数4:标题【消息内容的一部分】
    content = str(contents)  # 参数5:文本具体内容
    
    corpid = '12345'  # CorpID是企业号的标识
    corpsecret = '12345'  # corpsecretSecret是管理组凭证密钥
    try:
        accesstoken = gettoken(corpid,corpsecret)
        senddata(accesstoken,user,party,agent,subject,content)
    except Exception, e:
        print str(e) + "Error Please Check \"corpid\" or \"corpsecret\" Config" 
file.close

