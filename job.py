#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import urlencode
import xml.etree.ElementTree as ET
from writer import ResultSet
import re
from tools import req, HOST

def job_config_url(keyword, pageno=1):
    url_data = {
        'postchannel': '0000',
        'keyword': keyword,
        'keywordtype': '2',
        'jobarea': '020000', # 上海
        'pagesize': '200',
        'pageno': pageno,
        'accountid': '103712659', # 这个账号先写死
        'key': '188358252cf14b3121f2e9b274d84263592fa8de', # 不知道这是什么key
        'productname': '51job',
        'partner': '96b0485c6e84ec4dec5ebbf9ec9b2b6b',
        'uuid': 'c4a00ef4842aab24c1fd2ee92dbf3d8c',
        'version': '722',
        'guid': '9918238fa36ff89acbb3fae186a015b2'
    }
    url_encode = urlencode(url_data)
    url = HOST + 'search_job_list.php?' + url_encode
    return url

def search(keyword, page=1):
    '''获取一个公司的一页数据'''
    url = job_config_url(keyword, page)
    print url
    return req(url)

def get_coid(xml_text):
    '''获取公司coid'''   
    root = ET.fromstring(xml_text)
    coids = root.iter('coid')
    for ci in coids:
        return ci.text

def parse(xml_text=''):
    root = ET.fromstring(xml_text)
    sets_generator = root.iter('item')
    sets = []
    for s_g in sets_generator:
        sets.append(parse_item(s_g))
    return sets

parttern = re.compile(r'CDATA\[[\s\S]*?\]')
def filter_content(content):
    finds = re.findall(parttern, content)
    if len(finds) > 0:
        return finds[0][5][-1]
    else:
        return content


def parse_item(item):
    a_set = ResultSet('', '', '', '')
    item_generator = item.getchildren()
    for i_g in item_generator:
        if i_g.tag == 'jobname':
            a_set.job_title = filter_content(i_g.text).encode('utf-8')
        if i_g.tag == 'cddr':
            a_set.location = filter_content(i_g.text).encode('utf-8')
        if i_g.tag == 'coname':
            a_set.company = filter_content(i_g.text).encode('utf-8')
        if i_g.tag == 'providesalary':
            a_set.payment = filter_content(i_g.text).encode('utf-8')
    return a_set


def main():
    # result = search('游族网络')
    result = ''
    with open('./content.txt', 'r') as f:
        result = f.read()
    sg = parse(result)
    for s in sg:
        parse_item(s)
    

if __name__ == '__main__':
    # main()
    # with open('./content.txt', 'r') as f:
    #     result = f.read()
    # print filter_content(result)
    pass
