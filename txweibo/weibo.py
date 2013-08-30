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

def timestamp_datetime(value):
    format = '%Y-%m-%d %H:%M:%S'
    # value为传入的值为时间戳(整形)，如：1332888820
    value = time.localtime(value)
    ## 经过localtime转换后变成
    ## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=0)
    # 最后再经过strftime函数转换为正常日期格式。
    dt = time.strftime(format, value)
    return dt

def tweibo_test():
	oauth = OAuth2Handler()
	oauth.set_app_key_secret(APP_KEY, APP_SECRET, CALLBACK_URL)
	oauth.set_access_token(ACCESS_TOKEN)
	oauth.set_openid(OPENID)
	api = API(oauth)
	lo = 123.1011
	la = 31.1012
	search = []	
	try:
		temp = api.post.lbs__get_around_new(format="json",longitude = lo,latitude = la, pagesize = 25)
		page_ret = temp.data.pageinfo
		search.append(temp)
	except:
		print("No data")
	for page in range(1,10):
		try:
			temp = api.post.lbs__get_around_new(format="json", longitude = lo,latitude = la, pageinfo = page_ret, pagesize = 25 )
			page_ret = temp.data.pageinfo
			search.append(temp)
		except:
			print(" No next page")
	try:
		for page in search:
			for idx, tweet in enumerate(page.data.info):
				print "[%d], [%s],(%s),  %s" % (idx+1, tweet.location,timestamp_datetime(tweet.timestamp), tweet.text)
	except:
		pass

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
