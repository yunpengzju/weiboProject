# -*- coding:utf-8 -*- #
#! /usr/bin/env python

import time

#sys.path.insert(0, 'tweibo.zip')
from tweibo import *

# 换成你的 APPKEY
APP_KEY = "801058005"
APP_SECRET = "31cc09205420a004f3575467387145a7"
CALLBACK_URL = "https://test.open.t.qq.com"
# 请先按照 https://github.com/upbit/tweibo-pysdk/wiki/OAuth2Handler 的鉴权说明填写 ACCESS_TOKEN 和 OPENID
ACCESS_TOKEN = "e064789cdc8c80df50e0519d02882d70"
OPENID = "BCB210D551A94AF3D18D3C88E51668DB"
IMG_EXAMPLE = "example.png"

# 返回text是unicode，设置默认编码为utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def access_token_test():
    """ 访问get_access_token_url()的URL并授权后，会跳转callback页面，其中包含如下参数：
        #access_token=00000000000ACCESSTOKEN0000000000&expires_in=8035200&openid=0000000000000OPENID0000000000000&openkey=0000000000000OPENKEY000000000000&refresh_token=0000000000REFRESHTOKEN00000000&state=
    保存下其中的 access_token, openid 并调用
        oauth.set_access_token(access_token)
        oauth.set_openid(openid)
    即可完成 OAuth2Handler() 的初始化。可以记录 access_token 等信息
    """
    oauth = OAuth2Handler()
    oauth.set_app_key_secret(APP_KEY, APP_SECRET, CALLBACK_URL)
    print oauth.get_access_token_url()

def tweibo_test():
	oauth = OAuth2Handler()
	oauth.set_app_key_secret(APP_KEY, APP_SECRET, CALLBACK_URL)
	oauth.set_access_token(ACCESS_TOKEN)
	oauth.set_openid(OPENID)
	api = API(oauth)
	lo = 120
	la = 30
	search = []
	for page in range(1,10):
		temp = api.get.search__t(format="json", keyword="公益", pagesize = 30,page = page,contenttype = 0,sorttype = 0, msgtype = 1, searchtype = 8,starttime = 0, endtime = 0)
		search.append(temp)
	
	try:
		for page in search:
			for idx, tweet in enumerate(page.data.info):
				print "[%d], [%s],  %s" % (idx+1, tweet.location, tweet.text)
				print tweet.latitude
	except:
		pass
# 	print "state:  %d  message: %s" % (search.ret,search.msg)


# 	for lo in range(100,120):
# 		for la in range(30,50):
# 			search = api.get.search__t(format="json", keyword="天气", pagesize = 20,page = 1, longitude = lo, latitude = la, radius = 20000)
# 			print "state:  %d  message: %s" % (search.ret,search.msg)
# 			try:
# 				for idx, tweet in enumerate(search.data.info):
# 					print "[%d], %s" % (idx+1, tweet.text)
# 			except:
# 				pass
# 	tweet = api.post.t__add(format="json", content="天气", clientip="10.0.0.1", longitude = 120, latitude = 30)
# 	print(tweet.ret)
    #api = API(oauth, host="127.0.0.1", port=8888)       # Init API() with proxy
	
    # GET /t/show
    #tweet1 = api.get.t__show(format="json", id=301041004850688)
    #print ">> %s: %s" % (tweet1.data.nick, tweet1.data.text)

    # POST /t/add
    #content_str = "[from PySDK] %s says: %s" % (tweet1.data.nick, tweet1.data.origtext)
    #tweet2 = api.post.t__add(format="json", content=content_str, clientip="10.0.0.1")
    #print ">> time=%s, http://t.qq.com/p/t/%s" % (tweet2.data.time, tweet2.data.id)

    # GET /statuses/user_timeline
    #user_timeline = api.get.statuses__user_timeline(format="json", name="qqfarm", reqnum=3, pageflag=0, lastid=0, pagetime=0, type=3, contenttype=0)
    #for idx, tweet in enumerate(user_timeline.data.info):
    #    print "[%d] http://t.qq.com/p/t/%s, (type:%d) %s" % (idx+1, tweet.id, tweet.type, tweet.text)

    # UPLOAD /t/upload_pic
#     pic1 = api.upload.t__upload_pic(format="json", pic_type=2, pic=open(IMG_EXAMPLE, "rb"))
#     print ">> IMG: %s" % (pic1.data.imgurl)

    # POST /t/add_pic_url
#     content_str2 = "[from PySDK] add pic demo: %s, time %s" % (IMG_EXAMPLE, time.time())
#     pic_urls = "%s" % (pic1.data.imgurl)
#     tweet_pic1 = api.post.t__add_pic_url(format="json", content=content_str2, pic_url=pic_urls, clientip="10.0.0.1")
#     print ">> time=%s, http://t.qq.com/p/t/%s" % (tweet_pic1.data.time, tweet_pic1.data.id)
	
# 	print(tweet_mess1.ret)
if __name__ == '__main__':
    #access_token_test()
    tweibo_test()
