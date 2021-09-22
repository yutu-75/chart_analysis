# coding=utf-8
import json
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from bs4 import BeautifulSoup
from datetime import datetime
from config import crux_word
import re
import requests
import threading
import docx
from docx.oxml.ns import qn
from docx.shared import Pt
from pathlib import Path
import os
# from multiprocessing.dummy import Pool, Lock  # 线程池

with open('spider_url.json', 'r', encoding='utf-8') as f:
    url_dict = json.loads(f.read())
    f.close()


class get_text():
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        }

        self.d_dict = {
            '1': self.get_text1,
            '2': self.get_text2,
            '3': self.get_text3,
            '4': self.get_text4,
            '5': self.get_text5,
            '6': self.get_text6,
            '7': self.get_text7,

        }
        self.encoding = 'utf-8'

        self.n111 = 0
        self.str_text = 0
        self.url_dict = url_dict
        self.error_url_list = []                # 获取不到内容的url

    def get_soup(self, c_url):
        page_text = requests.get(url=c_url, headers=self.headers)
        url_status = page_text.status_code
        # print(url_status)
        page_text.encoding = self.encoding
        page_text = page_text.text
        soup = BeautifulSoup(page_text, 'lxml')
        return soup

    def content_analysis1(self,c_url,lock):

        with lock:
            self.n111 += 1
            print(self.n111)

        data_content = []
        start_time = datetime.now()
        page_text = requests.get(url=c_url, )

        page_text.encoding = 'utf-8'
        page_text = page_text.text

        soup = BeautifulSoup(page_text, 'lxml')
        tag = soup.select('.gknbxq_detail')
        print(tag[0].text)
        str_content = tag[0].text  # 文章的所有文本

        str_content = str_content.replace('\u2002', ' ')
        str_content = str_content.replace('\xa0', '\n')

        # print(str_content,type(str_content))

        n = 1
        serial_list = []
        mapping_list = []
        str_content_text = str_content.split('\n')
        str_content_text = [s_i.strip() for s_i in str_content_text if s_i]

        for i in str_content_text:  # 循环文本的每一行的数据
            i = i.strip()
            if len(i) < 1:
                continue
            n += 1

            def m_i(q, i_data):
                # print(q,i_data)
                if q in mapping_list:
                    # print('qwq')

                    a_index = mapping_list.index(q)
                    mapping_list[:a_index - 1].append(q)
                    del serial_list[a_index:]
                    serial_list.append(i_data)
                else:
                    mapping_list.append(q)
                    serial_list.append(i_data)
                # print(serial_list)
                # print()

            i_sign = ""
            if re.findall('^(第.*?章) ', i):  # 匹配    第一章
                # print(i)
                m_i('A', i)
                i_sign = "A"
            elif re.findall('^(第.*?条) ', i):  # 匹配    第一条
                # print(i)
                m_i('B', i)
                i_sign = "B"
            elif re.findall('^([一二三四五六七八九十]+、)', i):  # 匹配     一、
                # print(i)
                m_i('C', i)
                i_sign = "C"
            elif re.findall('^(（[一二三四五六七八九十]+）)', i):  # 匹配    （一）
                # print(i)
                m_i('D', i)
                i_sign = "D"
            elif re.findall('^(\d+\.)', i):  # 匹配     1.
                # print(i)
                m_i('E', i)
                i_sign = "E"
            elif re.findall('^(（\d+）)', i):  # 匹配    （1）
                # print(i)
                m_i('F', i)
                i_sign = "F"
            for c_word in crux_word:
                # if c_word in i:
                sum_i = i.count(c_word)
                if sum_i:

                    # print(serial_list,[c_word]+serial_list+[i])
                    if i not in serial_list:
                        data_content.append([c_word] + serial_list + [i] + [str(n)] + [str(sum_i)])
                    else:
                        data_content.append([c_word] + serial_list + [str(n)] + [str(sum_i)])
                    # print(data_content[-1][-3], '--------------', str_content_text.index(i))

                    # 段尾获取
                    end_text = ''

                    for d_c in str_content_text[str_content_text.index(i):]:  # 从当前段落往后循环

                        i_sign1 = ""
                        if re.findall('^(第.*?章) ', d_c):  # 匹配    第一章
                            i_sign1 = "A"
                        elif re.findall('^(第.*?条) ', d_c):  # 匹配    第一条
                            i_sign1 = "B"
                        elif re.findall('^([一二三四五六七八九十]+)', d_c):  # 匹配     一、

                            i_sign1 = "C"
                        elif re.findall('^(（[一二三四五六七八九十]+）)', d_c):  # 匹配    （一）
                            i_sign1 = "D"
                        elif re.findall('^(\d+\.)', d_c):  # 匹配     1.

                            i_sign1 = "E"
                        elif re.findall('^(（\d+）)', d_c):  # 匹配    （1）
                            i_sign1 = "F"
                        else:
                            i_sign1 = "G"
                        # print(mapping_list, i_sign, i_sign1)

                        if i_sign1 == 'G':
                            # end_text = d_c
                            data_content[-1].append(d_c)
                            break
                        if i_sign1 != i_sign:
                            break

        for q in data_content:
            pass
            with lock:
                print(c_url, q)
                self.str_text += 1

        print(datetime.now() - start_time)

    def content_analysis(self, str_content):

        start_time = datetime.now()
        n = 1
        data_content = []
        serial_list = []
        mapping_list = []
        str_content_text = str_content.split('\n')
        str_content_text = [s_i.strip() for s_i in str_content_text if s_i]

        for i in str_content_text:  # 循环文本的每一行的数据
            i = i.strip()
            if len(i) < 1:
                continue
            n += 1

            def m_i(q, i_data):
                # print(q,i_data)
                if q in mapping_list:
                    # print('qwq')

                    a_index = mapping_list.index(q)
                    mapping_list[:a_index - 1].append(q)
                    del serial_list[a_index:]
                    serial_list.append(i_data)
                else:
                    mapping_list.append(q)
                    serial_list.append(i_data)
                # print(serial_list)
                # print()

            i_sign = ""
            if re.findall('^(第.*?章) ', i):  # 匹配    第一章
                # print(i)
                m_i('A', i)
                i_sign = "A"
            elif re.findall('^(第.*?条) ', i):  # 匹配    第一条
                # print(i)
                m_i('B', i)
                i_sign = "B"
            elif re.findall('^([一二三四五六七八九十]+、)', i):  # 匹配     一、
                # print(i)
                m_i('C', i)
                i_sign = "C"
            elif re.findall('^(（[一二三四五六七八九十]+）)', i):  # 匹配    （一）
                # print(i)
                m_i('D', i)
                i_sign = "D"
            elif re.findall('^(\d+\.)', i):  # 匹配     1.
                # print(i)
                m_i('E', i)
                i_sign = "E"
            elif re.findall('^(（\d+）)', i):  # 匹配    （1）
                # print(i)
                m_i('F', i)
                i_sign = "F"
            for c_word in crux_word:
                # if c_word in i:
                sum_i = i.count(c_word)
                if sum_i:

                    # print(serial_list,[c_word]+serial_list+[i])
                    if i not in serial_list:
                        data_content.append([c_word] + serial_list + [i] + [str(n)] + [str(sum_i)])
                    else:
                        data_content.append([c_word] + serial_list + [str(n)] + [str(sum_i)])
                    # print(data_content[-1][-3], '--------------', str_content_text.index(i))

                    # 段尾获取
                    end_text = ''

                    for d_c in str_content_text[str_content_text.index(i):]:  # 从当前段落往后循环

                        i_sign1 = ""
                        if re.findall('^(第.*?章) ', d_c):  # 匹配    第一章
                            i_sign1 = "A"
                        elif re.findall('^(第.*?条) ', d_c):  # 匹配    第一条
                            i_sign1 = "B"
                        elif re.findall('^([一二三四五六七八九十]+)', d_c):  # 匹配     一、

                            i_sign1 = "C"
                        elif re.findall('^(（[一二三四五六七八九十]+）)', d_c):  # 匹配    （一）
                            i_sign1 = "D"
                        elif re.findall('^(\d+\.)', d_c):  # 匹配     1.

                            i_sign1 = "E"
                        elif re.findall('^(（\d+）)', d_c):  # 匹配    （1）
                            i_sign1 = "F"
                        else:
                            i_sign1 = "G"
                        # print(mapping_list, i_sign, i_sign1)

                        if i_sign1 == 'G':
                            # end_text = d_c
                            data_content[-1].append(d_c)
                            break
                        if i_sign1 != i_sign:
                            break
        for q in data_content:
            print(q)
        print(datetime.now() - start_time)

    @staticmethod
    def log_content(content):
        dir_path = Path(Path.cwd())/'log'
        if not Path.is_dir(dir_path):              # 判断是否有这个文件目录 没有则创建
            os.mkdir(dir_path)
        with open('./log/log.txt', 'a+', encoding='utf_8') as f:
            print(content)
            f.write(str(content)+'\n')


    def write_docx(self, title, str_content,file_name):

        dir_path = Path(Path.cwd())/'word'/file_name
        doc2 = docx.Document()  # 创建一个Document对象
        doc2.styles['Normal'].font.name = u'楷体'
        doc2.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'楷体')

        for i in str_content.split('\n'):
            p = doc2.add_paragraph(i)               # 增加一个paragraph
            p.style.font.name = '楷体'
            p.style.font.size = Pt(14)
            p.paragraph_format.first_line_indent = p.style.font.size * 2

        if not Path.is_dir(dir_path):              # 判断是否有这个文件目录 没有则创建
            os.mkdir(dir_path)
        a = '"'
        doc2.save(f'./word/{file_name}/{title.strip().replace(f"{a}","").replace(">",")").replace("<","(").replace("/","_")}.docx')  # 保存文档


        #
        # with open('qwq.docx','w',encoding='utd-8') as f:
        #     print()
        #     f.write('qwq')

    def error_url_write(self):
        dir_path = Path(Path.cwd())/'error'
        if not Path.is_dir(dir_path/'error.json'):              # 判断是否有这个文件目录 没有则创建
            os.mkdir(dir_path)

    def get_text1(self, url):
        """
        # 乌鲁木齐市人民政府
        :param url: http://www.urumqi.gov.cn/
        :return: title
        """
        file_name = '乌鲁木齐市人民政府'
        print(len(url),url)
        for c_url in url:
            start_time = datetime.now()
            page_text = requests.get(url=c_url, )

            page_text.encoding = 'utf-8'
            page_text = page_text.text
            soup = BeautifulSoup(page_text, 'lxml')
            title = soup.find('h2', class_='am-article-title am-text-left')     # 文件名字
            str_title = title.text
            print(title.text)
            tag = soup.select('#info_content')
            str_content = tag[0].text  # 文章的所有文本

            print(c_url)
            if str_content:
                self.write_docx(str_title, str_content, file_name)
            # break
            self.content_analysis(str_content)
            # print(str_content)
            end_time = datetime.now()
            print(end_time-start_time)

    def get_text2(self, url):
        """
        # 乌鲁木齐市发展和改革委员会
        :param url: http://www.wlmq.gov.cn/
        :return: title
        """
        file_name = '乌鲁木齐市发展和改革委员会'
        print(len(url), url)
        start_time = datetime.now()
        for c_url in url:

            soup = self.get_soup(c_url)
            title = soup.find('h1', class_='am-article-title am-text-center am-padding-vertical-sm')  # 文件名字
            str_title = title.text
            print(title.text)
            tag = soup.select('#info_content')
            str_content = tag[0].text  # 文章的所有文本

            print(c_url)
            if str_content:
                self.write_docx(str_title, str_content, file_name)
            # break
            self.content_analysis(str_content)
            # print(str_content)
        end_time = datetime.now()
        print(end_time - start_time)
        print(url)

    def get_text3(self, url):
        """
        # 乌鲁木齐市天山区人民政府
        :param url: http://www.xjtsq.gov.cn/
        :return: title
        """
        file_name = '乌鲁木齐市天山区人民政府'
        start_time = datetime.now()
        print(len(url),url)
        for c_url in url:
            print(c_url)

            soup = self.get_soup(c_url)
            title = soup.find('td', class_='titlestyle1400')  # 文件名字

            if not title:
                self.error_url_list.append(c_url)
                continue
            str_title = title.text
            print(str_title)
            try:
                tag = soup.select('#vsb_content')

                str_content = tag[0].text  # 文章的所有文本
            except Exception as e:
                tag = soup.select('#vsb_content_2')
                str_content = tag[0].text  # 文章的所有文本
                self.log_content(content=[e, c_url, '方式一未获取到文本内容！'])
            if str_content:
                self.write_docx(str_title, str_content, file_name)
            # break
            self.content_analysis(str_content)
            # print(str_content)
            end_time = datetime.now()
            print(end_time - start_time)
        print(url)

    def get_text4(self, url):
        """
        # 喀什地区行政公署
        :param url: http://www.kashi.gov.cn/
        :return: title
        """
        file_name = '喀什地区行政公署'
        start_time = datetime.now()

        for c_url in url:
            print(c_url)

            soup = self.get_soup(c_url)
            title = soup.find('h1', class_='xxgk-tt-title')  # 文件名字

            if not title:
                self.error_url_list.append(c_url)
                continue
            str_title = title.text
            print(str_title)
            tag = soup.select('#fontzoom')
            str_content = tag[0].text  # 文章的所有文本

            if str_content:
                self.write_docx(str_title, str_content, file_name)
            # break
            self.content_analysis(str_content)
            # print(str_content)
            end_time = datetime.now()
            print(end_time - start_time)

    def get_text5(self, url):
        """
        # 叶城县人民政府
        :param url: http://www.xjyc.gov.cn/
        :return: title
        """

        file_name = '叶城县人民政府'
        start_time = datetime.now()
        self.encoding = 'gb2312'
        for c_url in url:
            print(c_url)

            soup = self.get_soup(c_url)
            title = soup.title  # 文件名字


            if not title:
                self.error_url_list.append(c_url)
                continue
            str_title = title.text.split('-')[0]
            print(str_title)
            try:
                tag = soup.select('#fontzoom')
                str_content = tag[0].text  # 文章的所有文本
            except Exception as e:

                self.log_content(content=[e, str_title, c_url, '未获取到文本内容！'])
                continue
            if str_content:
                self.write_docx(str_title, str_content, file_name)
            # break
            self.content_analysis(str_content)
            # print(str_content)
        end_time = datetime.now()
        print(end_time - start_time)
        self.encoding = 'utf-8'

    def get_text6(self, url):
        """
        # 新疆维吾尔自治区工业和信息化厅
        :param url: http://gxt.xinjiang.gov.cn/
        :return: title
        """


        file_name = '新疆维吾尔自治区工业和信息化厅'
        start_time = datetime.now()
        n = 0
        for c_url in url:
            n += 1
            print(n)
            print(c_url)
            soup = self.get_soup(c_url)
            title = soup.h2  # 文件名字
            if not title:
                self.error_url_list.append(c_url)
                continue
            str_title = title.text
            print(str_title)
            try:
                tag = soup.select('.gknbxq_detail')
                str_content = tag[0].text  # 文章的所有文本
            except Exception as e:

                self.log_content(content=[e, str_title, c_url, '未获取到文本内容！'])
                continue
            if str_content:
                self.write_docx(str_title, str_content, file_name)
            # break
            self.content_analysis(str_content)
            # print(str_content)
            # return
        end_time = datetime.now()
        print(end_time - start_time)



    def get_text7(self, url):
        """
        # 新疆维吾尔自治区人民政府网
        :param url: http://www.xinjiang.gov.cn/
        :return: title
        """
        # print(len(url),url)

        file_name = '新疆维吾尔自治区人民政府网'
        start_time = datetime.now()
        n = 0
        for c_url in url:
            n += 1
            print(n)
            print(c_url)
            soup = self.get_soup(c_url)
            title = soup.h2  # 文件名字
            if not title:
                self.error_url_list.append(c_url)
                continue
            str_title = title.text
            print(str_title)
            try:
                tag = soup.select('.gknbxq_detail')
                str_content = tag[0].text  # 文章的所有文本
            except Exception as e:

                self.log_content(content=[e, str_title, c_url, '未获取到文本内容！'])
                continue
            if str_content:
                self.write_docx(str_title, str_content, file_name)
            # break
            self.content_analysis(str_content)
            # print(str_content)
            # return
        end_time = datetime.now()
        print(end_time - start_time)





        # 多线程代码
        # tp = ThreadPoolExecutor(50)
        # # lock = Lock()
        #
        # lock = threading.Lock()
        # for p_u_i in url:
        #     tp.submit(self.content_analysis1, p_u_i, lock)
        # tp.shutdown()

    def main(self):

        url_list = list(self.url_dict.values())

        # print(url_list[0])
        # self.get_text1(url_list[0])
        self.get_text2(url_list[1])
        # self.get_text3(url_list[2])
        # print(self.error_url_list)
        # self.get_text4(url_list[3])
        # self.get_text5(url_list[4])
        # self.get_text6(url_list[5])
        # self.get_text7(url_list[6])




        # print(self.url_list)
m = get_text()
m.main()
lock = threading.Lock()
# url = 'http://www.xinjiang.gov.cn/xinjiang/gfxwj/200808/7e47af6164fd468c8e43de306ed2e7ea.shtml'
# url1 = 'http://www.xinjiang.gov.cn/xinjiang/gfxwj/201104/dbcbf0b1cb0e49258ef2e4a1e3ce53a0.shtml'
# m.content_analysis1(url1,lock)