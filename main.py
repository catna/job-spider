#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tools
import writer
import time
import job
import company_info
import MySQLdb

import csv
import os

import logging

logging.basicConfig(level=logging.INFO,  
                    filename='log.log',  
                    filemode='a',  
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

pwd = os.path.abspath(os.curdir)
print pwd


connect = MySQLdb.connect(
    host='localhost',
    port = 3306,
    user='root',
    passwd='root',
    db ='jobs',
)


# sql = "INSERT INTO `company_info`(`coname`, `cosize`, `cotype`, `vocation`, `location`, `description`, `source`, `coid`, `cohash`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
sql = "SELECT * FROM `company_info_task_item` WHERE `status` = 0 LIMIT 10;"
update_sql = "UPDATE `company_info_task_item` SET `status` = 1 WHERE `id` = "
def get_item():
    cur = connect.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    cur.close()
    connect.commit()
    exsql = ''
    try:
        for i in result:
            if i[0] > 15:
                newcur = connect.cursor()
                exsql = update_sql + str(i[0]) + ';'
                newcur.execute(exsql)
                newcur.close()
                logging.info('------update str(i[0]) -----\n')
    except Exception, e:
        logging.info("执行MySQL: %s 时出错：%s" % (exsql, e))
        pass
    connect.commit()
    return result
    
def a_company_key_workflow(company_name):
    '''返回一个公司的数据结果'''
    a_job_list_xml = job.search(company_name)
    company_coid = job.get_coid(a_job_list_xml)
    a_company_xml = company_info.find(company_coid)
    a_company_set = company_info.parse_company(a_company_xml)
    return a_company_set

def job_workflow():
    '''查找公司id信息流程'''
    while True:
        items = get_item()
        for i in items:
            logging.info(i[1])
            a_set = a_company_key_workflow(i[1])
            writer.write_a_company_info(a_set)

def analysis_company():
    '''获取公司信息的逻辑'''
    # companys = prepare_keyword()
    # while len(companys):
    #     a_company_name = companys.pop()
    #     a_job_xml = job.search(a_company_name)
    #     a_company_id = job.get_coid(a_job_xml)
    #     a_company_id = '4190576'
    #     a_company_xml = company_info.find(a_company_id)
    #     a_company_set = company_info.parse_company(a_company_xml)
    #     writer.write_a_company_info(a_company_set)
    #     time.sleep(20)
    while True:
        start = writer.record_num()
        a_company_id = str(start)
        a_company_xml = company_info.find(a_company_id)
        a_company_set = company_info.parse_company(a_company_xml)
        # tools.post(a_company_set.post_object())
        writer.write_a_company_info(a_company_set)
        start = start + 1
        writer.record_num(start)
        # time.sleep(2)


def main():
    job_workflow()
    # analysis_company()
    pass


if __name__ == '__main__':
    main()
    pass
