#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import csv

path = os.path.abspath(os.path.curdir)
folder_name = path + '/Results'


if not os.path.exists(folder_name):
    os.mkdir(folder_name)

class ResultSet(object):
    _file_name = 'result_sets.csv'
    _fieldnames = ['company', 'job_title', 'payment', 'location']
    def __init__(self, company, job_title, payment, location):
        self.company = company
        self.job_title = job_title
        self.payment = payment
        self.location = location

class ResultOfCompany(object):
    _file_name = 'result_company.csv'
    _fieldnames = ['coid', 'coname', 'cotype', 'cosize', 'indtype1', 'indtype2', 'caddr', 'coinfo']
    
    def __init__(self, coid, coname, cotype, cosize, indtype1, indtype2, caddr, coinfo):
        self.coid = coid
        self.coname = coname
        self.cotype = cotype
        self.cosize = cosize
        self.indtype1 = indtype1
        self.indtype2 = indtype2
        self.caddr = caddr
        self.coinfo = coinfo

    def post_object(self, source=''):
#         {
#     "coname" : "coname",            // 名字
#     "cosize" : "cosize",            // 规模
#     "cotype" : "cotype",            // 性质
#     "vocation" : "vocation",        // 行业
#     "location" : "location",        // 位置
#     "description" : "description",  // 描述
#     "source" : "source",            // 来源
#     "coid" : "coid"                 // 编号
# }
        dic = {}
        dic['coid'] = self.coid
        dic['coname'] = self.coname
        dic['cotype'] = self.cotype
        dic['cosize'] = self.cosize
        dic['vocation'] = self.indtype1 + self.indtype2
        dic['location'] = self.caddr
        dic['description'] = self.coinfo
        dic['source'] = source
        return dic



def write_to_file(a_result):
    with open(folder_name + '/' + ResultSet._file_name, 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=ResultSet._fieldnames)
        writer.writeheader()
        writer.writerow(a_result.__dict__)

def write_a_company_info(a_result_of_company):
    with open(folder_name + '/' + ResultOfCompany._file_name, 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=ResultOfCompany._fieldnames)
        writer.writerow(a_result_of_company.__dict__)

def record_num(num=-1):
    if num == -1:
        with open('record', 'r') as record:
            start = int(record.read())
            record.close()
            return start
    else:
        with open('record', 'w+') as record:
            record.write(str(num))
            record.close()
            return num
    
        
        

def main():
    # aResult = ResultSet('公司', '职位', '薪酬', '位置')
    # write_to_file(aResult)
    a_company = ResultOfCompany('id', '公司', '类型', '规模', '分类1', '分类2', '地址', '信息')
    write_a_company_info(a_company)
    pass


if __name__ == '__main__':
    # main()
    pass
    