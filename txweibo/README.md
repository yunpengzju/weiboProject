# ��Ѷ΢��SDK for Python

�ο� @michaelliao �� [sinaweibopy](https://github.com/michaelliao/sinaweibopy) д�˸���Ѷ��API��������ͬ�Ķ�̬ [_http_call()](https://github.com/upbit/tweibo-pysdk/blob/master/tweibo.py#L90) ���÷�ʽ�����д�����������ά�����ص㡣

API����ϸʹ�÷�����[demo.py](https://github.com/upbit/tweibo-pysdk/blob/master/demo.py)���Ѳ��԰汾��Python 2.7

## FAQ
1. [OAuth2Handler(): OAuth2��Ȩ˵��](https://github.com/upbit/tweibo-pysdk/wiki/OAuth2Handler)
2. [demo.py���](https://github.com/upbit/tweibo-pysdk/wiki/demo.py%E8%AF%A6%E8%A7%A3)

***
demo.py��ʾ: �ϴ�example.png������΢��

```python
    # UPLOAD /t/upload_pic
    pic1 = api.upload.t__upload_pic(format="json", pic_type=2, pic=open(IMG_EXAMPLE, "rb"))
    print ">> IMG: %s" % (pic1.data.imgurl)

    # POST /t/add_pic_url
    content_str2 = "[from PySDK] add pic demo: %s, time %s" % (IMG_EXAMPLE, time.time())
    pic_urls = "%s" % (pic1.data.imgurl)
    tweet_pic1 = api.post.t__add_pic_url(format="json", content=content_str2, pic_url=pic_urls, clientip="10.0.0.1")
    print ">> time=%s, http://t.qq.com/p/t/%s" % (tweet_pic1.data.time, tweet_pic1.data.id)
```

![demo.py����Ч��](https://raw.github.com/wiki/upbit/tweibo-pysdk/images/demo.jpg)
