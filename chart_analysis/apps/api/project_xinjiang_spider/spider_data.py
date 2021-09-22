import requests
import os
import json
import re
from lxml import etree
from datetime import datetime
# from multiprocessing.dummy import Pool, Lock  # 线程池
from threading import Thread
import time
from config import crux_word
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from bs4 import BeautifulSoup
from threading import Lock
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
}
set_url = set()             # 去重后文章url地址
data_list = []              # 文章信息
del_title = '任免通知'       # 需要剔除的文章标题的关键字


class main:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        }
        self.headers7 = {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',

        }
        self.data_list = []
        self.set_url = set()
        self.del_title = '任免通知'
        self.encoding = 'utf-8'
        self.set_title = set()
        self.keyword = ['通知','指导意见','实施意见']

    def request_get(self,url):
        page_text = requests.get(url, headers=self.headers)
        page_text.encoding = self.encoding
        # print(page_text.status_code)
        if page_text.status_code == 404:
            return 0
        page_text = page_text.text

        tree = etree.HTML(page_text)

        return tree

    def analysis_tree1(self, tree):
        try:
            for i in range(1, 16):
                url = tree.xpath(f'/html/body/div[2]/div[3]/div/div/ul/li[{i}]/a/@href')

                if not url:
                    return 0
                if 'http' not in url[0]:
                    url = ['http://www.wlmq.gov.cn' + url[0]]
                title = tree.xpath(f'/html/body/div[2]/div[3]/div/div/ul/li[{i}]/a/text()')
                u_time = tree.xpath(f'/html/body/div[2]/div[3]/div/div/ul/li[{i}]/span/text()')
                if self.del_title in title[0]:
                    continue
                a = url + title + u_time
                self.data_list.append(a)
                self.set_url.add(url[0])
            else:
                return 1

        except Exception as e:
            print(e)

    def analysis_tree2(self, tree):
        try:
            for i in range(1, 25):
                url = tree.xpath(f'/html/body/div[1]/div[4]/div[1]/ul[1]/li[{i}]/a/@href')
                if not url:
                    return 0
                if 'http' not in url[0]:
                    url = ['http://www.wlmq.gov.cn' + url[0]]
                title = tree.xpath(f'/html/body/div[1]/div[4]/div[1]/ul[1]/li[{i}]/a/text()')

                u_time = tree.xpath(f'/html/body/div[1]/div[4]/div[1]/ul[1]/li[{i}]/span/text()')
                if self.del_title in title[0]:
                    continue
                a = url + title + u_time
                self.data_list.append(a)
                self.set_url.add(url[0])
            else:
                return 1

        except Exception as e:
            print(e)

    def analysis_tree3(self, tree):

        try:
            for i in range(1, 16):
                url = tree.xpath(f'/html/body/div[5]/div[3]/form[2]/div/table/tr[{i}]/td[2]/a/@href')
                if not url:
                    return 0
                if 'http' not in url[0]:
                    url = ['http://www.xjtsq.gov.cn/' + url[0].replace('../','')]
                title = tree.xpath(f'/html/body/div[5]/div[3]/form[2]/div/table/tr[{i}]/td[2]/a/text()')
                u_time = tree.xpath(f'/html/body/div[5]/div[3]/form[2]/div/table/tr[{i}]/td[5]/text()')
                if self.del_title in title[0]:
                    continue
                a = url + title + [u_time[0].strip()]
                self.data_list.append(a)
                self.set_url.add(url[0])
                print(a)
            else:
                return 1

        except Exception as e:
            print(e)

    def analysis_tree4(self, tree):

        try:
            for i in range(2, 18):
                url = tree.xpath(f'/html/body/div[2]/div[2]/div[2]/div/div[2]/div/table/tr[{i}]/td[2]/a/@href')
                if not url:
                    return 0
                if 'http' not in url[0]:
                    'http://www.kashi.gov.cn/'
                    url = ['http://www.kashi.gov.cn' + url[0].replace('../','')]
                title = tree.xpath(f'/html/body/div[2]/div[2]/div[2]/div/div[2]/div/table/tr[{i}]/td[2]/a/text()')
                u_time = tree.xpath(f'/html/body/div[2]/div[2]/div[2]/div/div[2]/div/table/tr[{i}]/td[4]/text()')
                if self.del_title in title[0]:
                    continue
                a = url + title + [u_time[0].strip()]
                self.data_list.append(a)
                self.set_url.add(url[0])
                print(a)
            else:
                return 1

        except Exception as e:
            print(e)

    def analysis_tree5(self, tree):

        try:
            for i in range(2, 32):
                url = tree.xpath(f'//*[@id="list"]/table/tr[{i}]/td[1]/div/a/@href')

                if not url:
                    return 0
                if 'http' not in url[0]:
                    url = ['http://www.xjyc.gov.cn' + url[0]]
                title = tree.xpath(f'//*[@id="list"]/table/tr[{i}]/td[1]/div/a/text()')
                u_time = tree.xpath(f'//*[@id="list"]/table/tr[{i}]/td[3]/text()')
                if self.del_title in title[0]:
                    continue
                a = url + title + u_time
                self.data_list.append(a)
                self.set_url.add(url[0])
                print(a)
            else:
                return 1

        except Exception as e:
            print(e)

    def analysis_tree6(self, tree):

        try:
            for i in range(1, 16):
                url = tree.xpath(f'//*[@id="wzlm"]/dl/dd[{i}]/a/@href')
                if not url:
                    return 0
                if 'http' not in url[0]:
                    url = ['http://gxt.xinjiang.gov.cn' + url[0]]
                title = tree.xpath(f'//*[@id="wzlm"]/dl/dd[{i}]/a/text()')
                u_time = tree.xpath(f'//*[@id="wzlm"]/dl/dd[{i}]/span/text()')
                if self.del_title in title[0]:
                    continue
                a = url + title + u_time
                self.data_list.append(a)
                self.set_url.add(url[0])
            else:
                return 1
        except Exception as e:
            print(e)


    def get_data1(self):
        """
        # 乌鲁木齐市人民政府
        # 规范性文件
        # url: http://www.urumqi.gov.cn/

        :return:
        """
        # 规范性文件
        start_time = datetime.now()
        url_1 = 'http://www.wlmq.gov.cn/info/iList.jsp?isSd=false&node_id=GKszf&cat_id=15282&tm_id=1004&cur_page=1'
        n = 0
        while True:
            n += 1
            url_4_n = f'http://www.wlmq.gov.cn/info/iList.jsp?isSd=false&node_id=GKszf&cat_id=15282&tm_id=1004&cur_page={n}'
            tree = self.request_get(url_4_n)
            sign = self.analysis_tree1(tree)
            if not sign:
                break

        # print(set_url)
        # print(len(data_list), data_list, len(data_list))
        end_time = datetime.now()
        print(end_time - start_time)
        return self.set_url



    def get_data2(self):
        """
        # 乌鲁木齐市发展和改革委员会
        # 政策法规
        # url: http://www.wlmq.gov.cn/info/iIndex.jsp?cat_id=15734

        :return:
        """
        # 政策法规
        start_time = datetime.now()
        url_1 = 'http://www.wlmq.gov.cn/info/iList.jsp?cat_id=15739'
        n = 0
        while True:
            n += 1
            url_4_n = f'http://www.wlmq.gov.cn/info/iList.jsp?cat_id=15739&cur_page={n}'
            tree = self.request_get(url_4_n)
            sign = self.analysis_tree2(tree)
            if not sign:
                break

        # print(set_url)
        # print(len(data_list), data_list, len(data_list))
        end_time = datetime.now()
        print(end_time - start_time)
        return self.set_url

    def get_data3(self):
        """
        # 乌鲁木齐市天山区人民政府
        # 政府信息公开目录
        # url: http://www.xjtsq.gov.cn/

        :return:
        """
        # 政府信息公开目录
        start_time = datetime.now()
        url_1 = 'http://www.xjtsq.gov.cn/open/guard/catalog/bjzf/tsqzfxxgkml.htm'
        tree = self.request_get(url_1)
        sign = self.analysis_tree3(tree)

        for i in range(35, 0, -1):
            print(i)
            # n += 1
            url_4_n = f'http://www.xjtsq.gov.cn/open/guard/catalog/bjzf/tsqzfxxgkml/{i}.htm'
            tree = self.request_get(url_4_n)
            sign = self.analysis_tree3(tree)
            if not sign:
                break

        end_time = datetime.now()
        print(end_time - start_time)
        return self.set_url

    def get_data4(self):
        """
        # 喀什地区行政公署
        # 法定主动公开内容（政策法规、重大决策）
        # url: http://www.kashi.gov.cn/

        :return:
        """
        # 法定主动公开内容（政策法规、重大决策）  --政策法规
        start_time = datetime.now()
        url_1 = 'http://www.kashi.gov.cn/Government/PublicInfoList.aspx?ThemeId=2&page='
        # 法定主动公开内容（政策法规、重大决策）  --重大决策
        url_1_1 = 'http://www.kashi.gov.cn/Government/PublicInfoList.aspx?ThemeId=3&page='
        for u_i in [url_1, url_1_1]:
            n = 0
            while True:
                n += 1
                url_4_n = u_i + str(n)
                tree = self.request_get(url_4_n)
                sign = self.analysis_tree4(tree)
                if not sign:
                    break

        end_time = datetime.now()
        print(end_time - start_time)
        return self.set_url

    def get_data5(self):
        """
        # 叶城县人民政府
        # 政府信息公开——法定主动公开内容  -政策法规 -重大决策 -重点信息公开
        # url: http://www.xjyc.gov.cn/

        :return:
        """
        start_time = datetime.now()
        self.encoding = 'gb2312'

        # 政策法规
        url_1 = 'http://www.xjyc.gov.cn/html/zcfg/index'

        # 重大决策
        url_2 = 'http://www.xjyc.gov.cn/html/zdjc/index'

        # 重点信息公开
        url_3 = 'http://www.xjyc.gov.cn/html/shfw/index'

        for u_i in [url_1, url_2, url_3]:
            n = 0
            while True:
                n += 1
                if n == 1:
                    url_4_n = u_i + '.html'
                else:

                    url_4_n = u_i + f'_{n}.html'
                print(url_4_n)
                tree = self.request_get(url_4_n)
                sign = self.analysis_tree5(tree)
                if not sign:
                    break

        end_time = datetime.now()
        print(end_time - start_time)
        self.encoding = 'utf-8'
        return self.set_url

    def get_data6(self):
        """
        # 新疆维吾尔自治区工业和信息化厅
        # 政府信息公开——履约依据、规划统计、重点领域信息公开
        # url: http://gxt.xinjiang.gov.cn/

        :return:
        """
        start_time = datetime.now()

        # 履职依据
        ## 三定方案
        url_1 = 'http://gxt.xinjiang.gov.cn/gxt/sdfa/zfxxgk_gknrz.shtml'
        tree = self.request_get(url_1)
        sign = self.analysis_tree6(tree)

        ## 政策文件
        url_2 = 'http://gxt.xinjiang.gov.cn/gxt/gfxwj/zfxxgk_gknrz.shtml'
        tree = self.request_get(url_2)
        sign = self.analysis_tree6(tree)

        ## 政策解读
        url_3 = 'http://gxt.xinjiang.gov.cn/gxt/jdhy/zfxxgk_gknrz.shtml'
        url_3_1 = 'https://gxt.xinjiang.gov.cn/gxt/jdhy/zfxxgk_gknrz_2.shtml'
        url_list = [url_3, url_3_1]
        for u_i in url_list:
            tree = self.request_get(u_i)
            sign = self.analysis_tree6(tree)

        # 规划统计
        url_4 = 'https://gxt.xinjiang.gov.cn/gxt/ghtj/zfxxgk_gknrz.shtml'
        tree = self.request_get(url_4)
        self.analysis_tree6(tree)
        url_4_1 = 'https://gxt.xinjiang.gov.cn/gxt/ghtj/zfxxgk_gknrz_2.shtml'
        n = 1
        while True:
            n += 1
            url_4_n = f'https://gxt.xinjiang.gov.cn/gxt/ghtj/zfxxgk_gknrz_{n}.shtml'
            tree = self.request_get(url_4_n)
            if tree == 0:
                break
            self.analysis_tree6(tree)

        # 重点领域信息公开
        url_5 = 'https://gxt.xinjiang.gov.cn/gxt/zdxxgk/zfxxgk_gknrz.shtml'
        tree = self.request_get(url_5)
        self.analysis_tree6(tree)
        url_5_1 = 'https://gxt.xinjiang.gov.cn/gxt/zdxxgk/zfxxgk_gknrz_2.shtml'
        n = 1
        while True:
            n += 1
            url_4_n = f'https://gxt.xinjiang.gov.cn/gxt/zdxxgk/zfxxgk_gknrz_{n}.shtml'
            tree = self.request_get(url_4_n)
            if tree == 0:
                break
            self.analysis_tree6(tree)

        return self.set_url

    def get_data7(self):
        """
        # 新疆维吾尔自治区人民政府网
        # 政府信息公开        搜索search  关键字: 通知、实施意见、指导意见
        # url: http://www.xinjiang.gov.cn/

        :return:
        """
        start_time = datetime.now()


        bid_url = 'http://www.xinjiang.gov.cn/interface-cms/qryManuscriptByWebsiteId'  # json数据获取url

        for k_w in self.keyword:
            serial_number = 1
            print('*************')
            len(self.set_url)
            sign = True
            pageNum = 0
            while sign:
                pageNum += 1
                payload = {
                    'channelId': ['282d91208a28467baa4bfec472c0b3ba'],
                    'pageNum': pageNum,
                    'pageSize': 15,
                    'title': k_w,
                    'websiteId': "2a4092ca8c2a4255bfec9f13f114aba6",
                }
                # print(json.dumps(payload))
                page_text = requests.post(url=bid_url, headers=self.headers7, data=json.dumps(payload))
                page_text.encoding = 'utf-8'
                page_json = page_text.json()

                if len(page_json['results']) == 0:
                    sign = False
                    break
                for p_data in page_json['results']:
                    title = p_data['title']
                    publishedTime = p_data['publishedTime']
                    if 'http' in p_data['url']:
                        url = p_data['url']
                    else:
                        url = 'http://www.xinjiang.gov.cn' + p_data['url']
                    if title in self.set_title or url in set_url or '任免通知' in title:
                        continue
                    else:
                        self.set_title.add(title)
                        self.set_url.add(url)
                        self.data_list.append([url, title, publishedTime])

                        print(serial_number,k_w,[url, title, publishedTime])
                        serial_number += 1

        end_time = datetime.now()
        print(end_time - start_time)
        return self.set_url


if __name__ == '__main__':
    m = main()
    url_list = {}
    set_url = m.get_data1()       # 60        乌鲁木齐市人民政府
    url_list['1'] = list(set_url)
    m.set_url = set()

    set_url = m.get_data2()       # 20        乌鲁木齐市发展和改革委员会
    url_list['2'] = list(set_url)
    m.set_url = set()

    set_url = m.get_data3()       # 526       乌鲁木齐市天山区人民政府
    url_list['3'] = list(set_url)
    m.set_url = set()

    set_url = m.get_data4()       # 173       喀什地区行政公署
    url_list['4'] = list(set_url)
    m.set_url = set()

    set_url = m.get_data5()       # 637       叶城县人民政府
    url_list['5'] = list(set_url)
    m.set_url = set()

    set_url = m.get_data6()       # 1029      新疆维吾尔自治区工业和信息化厅
    url_list['6'] = list(set_url)
    m.set_url = set()

    set_url = m.get_data7()       # 1473      新疆维吾尔自治区人民政府网
    url_list['7'] = list(set_url)
    m.set_url = set()

    with open('spider_url.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(url_list))

    with open('data_list.txt', 'w', encoding='utf-8') as f:
        for d_i in m.data_list:
            f.write(str(d_i)+'\n')
