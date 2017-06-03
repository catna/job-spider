#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tools
import writer
import time
import job
import company_info

def prepare_keyword():
    keyword = ['游族网络']
    return keyword
    
def job_workflow():
    '''存储工作信息流程'''
    company_names = prepare_keyword()
    while len(company_names):
        a_company_name = company_names.pop()
        page = 1
        while page <= 10:
            a_job_list_page_xml = job.search(a_company_name, page)
            a_job_list_parse_results = job.parse(a_job_list_page_xml)
            for a_job_info in a_job_list_parse_results:
                writer.write_to_file(a_job_info)
            page = page + 1
            time.sleep(20)
    pass

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
    # job_workflow()
    analysis_company()
    pass


if __name__ == '__main__':
    main()
