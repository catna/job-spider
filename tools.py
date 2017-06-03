#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json

# url = "http://api.51job.com/api/job/search_job_list.php?postchannel=0000&keyword=%E6%B8%B8%E6%97%8F%E7%BD%91%E7%BB%9C&keywordtype=2&jobarea=020000&pagesize=200&pageno=2&accountid=103712659&key=188358252cf14b3121f2e9b274d84263592fa8de&productname=51job&partner=96b0485c6e84ec4dec5ebbf9ec9b2b6b&uuid=c4a00ef4842aab24c1fd2ee92dbf3d8c&version=722&guid=9918238fa36ff89acbb3fae186a015b2"
HOST = "http://api.51job.com/api/job/"

def req(url):
    headers = {
        "User-Agent": "51job-iphone-client",
        "Accept-Language": "zh-cn",
        "Accept-Encoding": "gzip,deflate",
        "Connection": "keep-alive",
        "Accept": "*/*"
    }
    return requests.get(url, headers=headers).content

def post(body={}):
    headers = {
        "Content-Type" : "application/json"
    }
    return requests.post('http://47.92.131.98:8001/company/info', data=json.dumps(body), headers=headers)

def main():
    dic = {
        "coname" : "coname",           
        "cosize" : "cosize",           
        "cotype" : "cotype",           
        "vocation" : "vocation",       
        "location" : "location",       
        "description" : "description", 
        "source" : "source",           
        "coid" : "coid"                
    }
    post(dic)

if __name__ == '__main__':
    main()