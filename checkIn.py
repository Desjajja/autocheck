#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from typing import Dict
import time


# In[ ]:


def redata(formdata: Dict) -> str:#返回url编码的数据
    redata = parse.urlencode(formdata)
    return redata


# In[ ]:


url1 = "http://jc.ncu.edu.cn/gate/student/getPreSignInfo"
header1 = {
        "Host": "jc.ncu.edu.cn",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1316.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat",
        "token": "eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJlY2hpc2FuIiwic3ViIjoiNjExMjExOTAzMCIsImlhdCI6MTYxMTE5MzU3OH0.NmZGEpyxnfxhyuuqfOSicOsxW94Y3NhJNjbYC3vc0sBoRp68fP4h6PtrhgXASHENrXbmpQQaGMcIkT81Mm7T5A",
        "Referer": r"http://jc.ncu.edu.cn/?code=5iZJrEFIZOrYmYTmgxg4r0VqmpyDsMCB6XLit_fYxio&state=STATE",
        "Accept-Encoding": "gzip, deflate"
    }


# In[ ]:


def request_preSign(url1: str, header: Dict):#上一次登录查询
    r = requests.get(url1, headers=header)
    return r


# In[ ]:


res = request_preSign(url1, header1)
print(res.text)


# In[ ]:


url2 = "http://jc.ncu.edu.cn/gate/student/signIn"
header2 = {
    "Host": "jc.ncu.edu.cn",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1316.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat",
    "token": "eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJlY2hpc2FuIiwic3ViIjoiNjExMjExOTAzMCIsImlhdCI6MTYxMTE5MzU3OH0.NmZGEpyxnfxhyuuqfOSicOsxW94Y3NhJNjbYC3vc0sBoRp68fP4h6PtrhgXASHENrXbmpQQaGMcIkT81Mm7T5A",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Referer": "http://jc.ncu.edu.cn/?code=5iZJrEFIZOrYmYTmgxg4r0VqmpyDsMCB6XLit_fYxio&state=STATE",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4"
          }
data_home = "inChina=%E6%98%AF&addressProvince=%E6%B2%B3%E5%8C%97%E7%9C%81&addressCity=%E7%9F%B3%E5%AE%B6%E5%BA%84%E5%B8%82&temperatureStatus=%E6%AD%A3%E5%B8%B8&temperature=0&isIll=%E5%90%A6&closeHb=%E5%90%A6&closeIll=%E5%90%A6&healthDetail=%E6%97%A0%E5%BC%82%E5%B8%B8&isIsolation=%E5%90%A6&isolationPlace=%E6%97%A0&userId=6112119030&addressInfo=%E5%A1%94%E5%8D%97%E8%B7%AF%E9%9B%85%E6%B8%85%E8%8B%91%E5%B0%8F%E5%8C%BA2-1-701&isGraduate=%E5%90%A6&healthStatus=%E6%97%A0%E5%BC%82%E5%B8%B8&isIsolate=%E5%90%A6&isolatePlace=%E6%97%A0"
while True:
    r = requests.post(url2, headers=header2, data=data_home)
    print(r.text)
    time.sleep(60)

