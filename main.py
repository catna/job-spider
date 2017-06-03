#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tools
import writer
import time
import job
import company_info

def prepare_keyword():
    keyword = '游族网络'
    return keyword
    
def a_company_key_workflow(company_name):
    '''返回一个公司的数据结果'''
    a_job_list_xml = job.search(company_name)
    company_coid = job.get_coid(a_job_list_xml)
    a_company_xml = company_info.find(company_coid)
    a_company_set = company_info.parse_company(a_company_xml)
    return a_company_set.post_object(source='51job_search')

def job_workflow():
    '''查找公司id信息流程'''
    while  True:
        company_name = prepare_keyword()
        a_set = a_company_key_workflow(company_name)
        # tools.post(a_company_set.post_object())
        time.sleep(2)

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
        tools.post(a_company_set.post_object())
        start = start + 1
        writer.record_num(start)
        time.sleep(2)


def main():
    job_workflow()
    # analysis_company()
    pass


if __name__ == '__main__':
    main()
