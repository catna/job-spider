#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tools import HOST, req
import xml.etree.ElementTree as ET
from urllib import urlencode
import writer

# url = 'api.51job.com/api/job/get_co_info.php?coid=2284274&productname=51job&partner=96b0485c6e84ec4dec5ebbf9ec9b2b6b&uuid=c4a00ef4842aab24c1fd2ee92dbf3d8c&version=722&guid=9918238fa36ff89acbb3fae186a015b2'

def company_config_url(coid):
    url_data = {
        'coid': coid,
        # 'keyword': keyword,
        # 'keywordtype': '2',
        # 'jobarea': '020000', # 上海
        # 'pagesize': '200',
        # 'pageno': pageno,
        # 'accountid': '103712659', # 这个账号先写死
        # 'key': '188358252cf14b3121f2e9b274d84263592fa8de', # 不知道这是什么key
        'productname': '51job',
        'partner': '96b0485c6e84ec4dec5ebbf9ec9b2b6b',
        'uuid': 'c4a00ef4842aab24c1fd2ee92dbf3d8c',
        'version': '722',
        'guid': '9918238fa36ff89acbb3fae186a015b2'
    }
    url_encode = urlencode(url_data)
    url = HOST + 'get_co_info.php?' + url_encode
    return url

def parse_company(xml_text):
    '''解析公司xml文本'''
    a_company = writer.ResultOfCompany('' ,'', '', '', '', '', '', '')
    root = ET.fromstring(xml_text)
    root_childs = list(root)
    for child in root_childs:
        if child.tag == 'resultbody':
            for info in list(child):
                if hasattr(a_company, info.tag):
                    try:
                        setattr(a_company, info.tag, info.text.encode('utf-8'))
                    except Exception:
                        pass
                    
    a_company.coinfo = ''
    return a_company

def find(coid):
    '''获取一个公司的信息'''
    url = company_config_url(coid)
    print url
    return req(url)
