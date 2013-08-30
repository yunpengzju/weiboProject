# -*- coding:utf-8 -*- #
#! /usr/bin/env python

import time
#sys.path.insert(0, 'tweibo.zip')
from tweibo import *
import cPickle

# 验证信息
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
	lo = 120
	la = 30
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
				print "[%d], [longitude:%s, latitude:%s] [%s],(%s),  %s" % (idx+1,tweet.longitude,tweet.latitude,tweet.location,timestamp_datetime(tweet.timestamp), tweet.text)
		f = open("data/mydata","wb")
		cPickle.dump(search,f)
		f.close()
	except:
		pass
	
	

if __name__ == '__main__':
    #access_token_test()
    tweibo_test()
