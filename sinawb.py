# -*- coding:utf-8 -*- #
#! /usr/bin/env python
from weibo import APIClient
import jieba
import nltk

APP_KEY = '2861702996'                               # app key
APP_SECRET = '0bb109636d9aaa9e5d6ba6fbbea42eff'      # app secret
CALLBACK_URL = 'https://github.com'                  # callback url

CODE = '8716fdd98041882a87d6c144bf47a4d1'            # 从访问callback_url时获得的code，用于获取acess_token

ACCESS_TOKEN = '2.009lLIGEwf6fHD554ef1df6a3BpjPD'	 # 和expires_in一起，七天内有效
EXPIRES_IN = '1537535161'

# 以下两个常量用于测试特定时间段的微博信息
START_TIME =  1379064600        # 2013.9.13 杭州大暴雨
END_TIME   =  1379071800
# 以下两个常量用于测试特定地点情况
LONG = 120.1457550317383
LAT  = 30.243664449817462

# get_url函数获取验证所需url，访问此url会提示登录新浪微博并重定向到另一url。从该url可获取后面步骤所需的code
def get_url():
	client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET,
                   redirect_uri=CALLBACK_URL)
	url = client.get_authorize_url()
	print url

# 此函数获取access_token
def get_access_token():
	client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET,
                   redirect_uri=CALLBACK_URL)
	r = client.request_access_token(CODE)
	access_token = r.access_token  # access token，e.g., abc123xyz456
	expires_in = r.expires_in      # token expires in
	print access_token
	print expires_in

# 调用api获取所需微博信息
def use_api():
	client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET,
                   redirect_uri=CALLBACK_URL)
	client.set_access_token(ACCESS_TOKEN, EXPIRES_IN)

	results = []
	lines = ""
	for page_num in range(1,20):		# 获取前10页结果
		temp = client.place.nearby_timeline.get(long = LONG, lat = LAT, page = page_num, starttime = START_TIME, endtime = END_TIME)
		results.append(temp)
	weibos = preProcess(results)
	for id, weibo in enumerate(weibos):
		print "%d, %s  " % (id,weibo.text)
		lines += weibo.text
	fenci(lines)
	
# 以下函数对返回的多页微博信息进行统一筛选处理
def preProcess(lists):
	weibos = []
	for list in lists:
		for weibo in list.statuses:
			if isUseful(weibo.text):
				weibos += [weibo]
# 	for id, weibo in enumerate(weibos):			# for test
# 		print "%d, %s  " % (id,weibo.text)
	return weibos	

def isUseful(text):
	KEYWORDS = ["雨","雷","水","海","淹"]
	KEY2 = ["深","涨"]
	for key in KEYWORDS:
		if key in text.encode('utf-8'):
			return True
	return False
	
	
#以下程序试对抓取到的微博做分词处理
def fenci(str = ""):
	words     = []
	seg_list  = jieba.cut(str, cut_all=False)
	
	for word in seg_list:
		if len(word) > 1:
			words += [word]
	print "高频词："
	freq = nltk.FreqDist(words)
	t = freq.keys()[:70]
	for word in t:
		print word
		
	
if __name__ == '__main__':
	#get_url()
    #get_access_token()
    use_api()
