# -*- coding:utf-8 -*- #
#! /usr/bin/env python

import time
from tweibo import *
import cPickle

# 验证信息
APP_KEY = "801058005"
APP_SECRET = "31cc09205420a004f3575467387145a7"
CALLBACK_URL = "https://test.open.t.qq.com"
ACCESS_TOKEN = "e064789cdc8c80df50e0519d02882d70"
OPENID = "BCB210D551A94AF3D18D3C88E51668DB"
IMG_EXAMPLE = "example.png"

# 默认字符集utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 用户验证
def access_token_test():
    oauth = OAuth2Handler()
    oauth.set_app_key_secret(APP_KEY, APP_SECRET, CALLBACK_URL)
    print oauth.get_access_token_url()

# 将系统时间戳转换成标准的日期格式
def timestamp_datetime(value):
    format = '%Y-%m-%d %H:%M:%S'
    # value为传入的值为时间戳(整形)，如：1332888820
    value = time.localtime(value)
    # 经过strftime函数转换为正常日期格式。
    dt = time.strftime(format, value)
    return dt

# 通过api获取微博
def tweibo_test():
	oauth = OAuth2Handler()
	oauth.set_app_key_secret(APP_KEY, APP_SECRET, CALLBACK_URL)
	oauth.set_access_token(ACCESS_TOKEN)
	oauth.set_openid(OPENID)
	api = API(oauth)
	
	lo = 120  # 测试时只固定尝试了一个经纬度值的微博情况。实际使用时可使用嵌套的循环遍历一批经纬度
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
		cPickle.dump(search,f)      # 方便实验，将抓取到的json格式信息存到文件中保存；未来实际操作应存入数据库中
		f.close()
	except:
		pass
	
if __name__ == '__main__':
    #access_token_test()
    tweibo_test()
