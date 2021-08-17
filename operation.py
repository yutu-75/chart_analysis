# coding:utf-8
a = ['奖励', '补贴', '补助', '资助', '税费', '税收', '纳税', '纳税额', '缴纳入库地方级税收', '纳税地方贡献额留成', '纳税地方留成', '地方税收贡献额', '税收地方留成',
     '地方财政留成',
     '财政贡献地方留成', '项目库', '名录库', '备选库', '资格库', '储备库', '培育库', '目录库', '目录', '注册', '登记', '设立分支机构', '设立法人机构', '设立子公司',
     '设有分支机构', '设有法人机构', '设有子公司', '迁出', '迁离', '外迁', '转出', '追回', '返还', '退还', '收回', '追缴', '承诺', '优先给予', '优先支持',
     '优先扶持',
     '优先安排', '优先推荐', '优先采购', '优先选用', '优先使用', '优先考虑', '优先选择', '优先选购', '重点支持', '重点扶持', '领军企业', '龙头', '知名', '骨干', '推荐',
     '本土', '本地', '区内']



a1 = []
for i in a:
    a1.append(i+'1')
print(a1)
#
#
# str_ci = "奖励、补贴、补助、资助、税费、税收、纳税、纳税额、缴纳入库地方级税收、纳税地方贡献额留成、纳税地方留成、地方税收贡献额、税收地方留成、地方财政留成、财政贡献地方留成、项目库、名录库、备选库、资格库、储备库、培育库、目录库、目录、注册、登记、设立分支机构、设立法人机构、设立子公司、设有分支机构、设有法人机构、设有子公司、迁出、迁离、外迁、转出、追回、返还、退还、收回、追缴、承诺、优先给予、优先支持、优先扶持、优先安排、优先推荐、优先采购、优先选用、优先使用、优先考虑、优先选择、优先选购、重点支持、重点扶持、领军企业、龙头、知名、骨干、推荐、本土、本地、区内"
# a = ['奖励', '补贴', '补助', '资助', '税费', '税收', '纳税', '纳税额', '缴纳入库地方级税收', '纳税地方贡献额留成', '纳税地方留成', '地方税收贡献额', '税收地方留成', '地方财政留成', '财政贡献地方留成', '项目库', '名录库', '备选库', '资格库', '储备库', '培育库', '目录库', '目录', '注册', '登记', '设立分支机构', '设立法人机构', '设立子公司', '设有分支机构', '设有法人机构', '设有子公司', '迁出', '迁离', '外迁', '转出', '追回', '返还', '退还', '收回', '追缴', '承诺', '优先给予', '优先支持', '优先扶持', '优先安排', '优先推荐', '优先采购', '优先选用', '优先使用', '优先考虑', '优先选择', '优先选购', '重点支持', '重点扶持', '领军企业', '龙头', '知名', '骨干', '推荐', '本土', '本地', '区内']
#
#
#
# from docx import Document
# from datetime import datetime, timedelta
# import uuid
# from multiprocessing.dummy import Pool  # 线程池
# from multiprocessing import Process,Lock
# look = Lock() #创建锁
# print(uuid.uuid1())
# from threading import Thread
#
#
#
# from PyPDF2 import PdfFileWriter, PdfFileReader
#
#
# [{'id': 1, 'name': '登记', 'str_page': '4、33、52、74、75', 'str_sum': 5, 'children': [{'str_page': 4, 'str_sum': 1, 'id': 100}, {'str_page': 33, 'str_sum': 1, 'id': 101}, {'str_page': 52, 'str_sum': 1, 'id': 102}, {'str_page': 74, 'str_sum': 1, 'id': 103}, {'str_page': 75, 'str_sum': 1, 'id': 104}]}, {'id': 2, 'name': '承诺', 'str_page': '4、22、33、38、58、59、60、73', 'str_sum': 13, 'children': [{'str_page': 4, 'str_sum': 1, 'id': 200}, {'str_page': 22, 'str_sum': 1, 'id': 201}, {'str_page': 33, 'str_sum': 1, 'id': 202}, {'str_page': 38, 'str_sum': 1, 'id': 203}, {'str_page': 58, 'str_sum': 1, 'id': 204}, {'str_page': 59, 'str_sum': 6, 'id': 205}, {'str_page': 60, 'str_sum': 1, 'id': 206}, {'str_page': 73, 'str_sum': 1, 'id': 207}]}, {'id': 3, 'name': '本地', 'str_page': '13', 'str_sum': 2, 'children': [{'str_page': 13, 'str_sum': 2, 'id': 300}]}, {'id': 4, 'name': '目录', 'str_page': '20', 'str_sum': 1, 'children': [{'str_page': 20, 'str_sum': 1, 'id': 400}]}, {'id': 5, 'name': '注册', 'str_page': '21、22、23、38', 'str_sum': 6, 'children': [{'str_page': 21, 'str_sum': 1, 'id': 500}, {'str_page': 22, 'str_sum': 1, 'id': 501}, {'str_page': 23, 'str_sum': 2, 'id': 502}, {'str_page': 38, 'str_sum': 2, 'id': 503}]}, {'id': 6, 'name': '退还', 'str_page': '22、35、46、62、63、69', 'str_sum': 10, 'children': [{'str_page': 22, 'str_sum': 2, 'id': 600}, {'str_page': 35, 'str_sum': 1, 'id': 601}, {'str_page': 46, 'str_sum': 1, 'id': 602}, {'str_page': 62, 'str_sum': 3, 'id': 603}, {'str_page': 63, 'str_sum': 2, 'id': 604}, {'str_page': 69, 'str_sum': 1, 'id': 605}]}, {'id': 7, 'name': '区内', 'str_page': '27、30、43', 'str_sum': 5, 'children': [{'str_page': 27, 'str_sum': 1, 'id': 700}, {'str_page': 30, 'str_sum': 2, 'id': 701}, {'str_page': 43, 'str_sum': 2, 'id': 702}]}, {'id': 8, 'name': '纳税', 'str_page': '58', 'str_sum': 3, 'children': [{'str_page': 58, 'str_sum': 3, 'id': 800}]}, {'id': 9, 'name': '税收', 'str_page': '73', 'str_sum': 1, 'children': [{'str_page': 73, 'str_sum': 1, 'id': 900}]}]
#
# import PyPDF2
# import pdfplumber
# d_a = {'奖励': [0], '补贴': [0], '补助': [0], '资助': [0], '税费': [0], '税收': [0], '纳税': [0], '纳税额': [0], '缴纳入库地方级税收': [0], '纳税地方贡献额留成': [0], '纳税地方留成': [0], '地方税收贡献额': [0], '税收地方留成': [0], '地方财政留成': [0], '财政贡献地方留成': [0], '项目库': [0], '名录库': [0], '备选库': [0], '资格库': [0], '储备库': [0], '培育库': [0], '目录库': [0], '目录': [0], '注册': [0], '登记': [0], '设立分支机构': [0], '设立法人机构': [0], '设立子公司': [0], '设有分支机构': [0], '设有法人机构': [0], '设有子公司': [0], '迁出': [0], '迁离': [0], '外迁': [0], '转出': [0], '追回': [0], '返还': [0], '退还': [0], '收回': [0], '追缴': [0], '承诺': [0], '优先给予': [0], '优先支持': [0], '优先扶持': [0], '优先安排': [0], '优先推荐': [0], '优先采购': [0], '优先选用': [0], '优先使用': [0], '优先考虑': [0], '优先选择': [0], '优先选购': [0], '重点支持': [0], '重点扶持': [0], '领军企业': [0], '龙头': [0], '知名': [0], '骨干': [0], '推荐': [0], '本土': [0], '本地': [0], '区内': [0]}
#
# {'承诺': [9, '第41段落', '第57段落', '第159段落', '第262段落', '第374段落', '第382段落', '第384段落', '第388段落', '表格内容:承诺'], '资助': [6, '第33段落', '第34段落', '第77段落', '第184段落', '第295段落', '表格内容:资助'], '注册': [4, '第15段落', '第81段落', '第188段落', '第299段落'], '登记': [1, '表格内容:登记'], '区内': [1, '第15段落']}
#
# def extract_content_docx(path):
#     s_time = datetime.now()
#     print(s_time)
#     d_a = {}
#     d_list = []
#
#     document = Document(path)  # 读入文件
#
#     tables = document.tables  # 获取文件中的表格集
#     row_content = ''
#     for table in tables[:]:
#         for i, row in enumerate(table.rows[:]):  # 读每行
#             for cell in row.cells[:]:  # 读一行中的所有单元格
#                 c = cell.text
#                 row_content += c
#
#     for i in range(len(document.paragraphs)):
#         content = document.paragraphs[i].text
#         for t in a:
#
#             str_sum = str(content).count(t)  # 每一页字符出现的次数
#             if str_sum:
#                 if d_a.get(t, False):
#                     d_a[t]['str_sum'] += str_sum
#                     d_a[t]['str_page'] += f'、{i}'
#
#                     d_a[t]['children'] += [{'str_page': i, 'str_sum': str_sum}]
#
#                 else:
#                     d_a[t] = {'str_page': str(i), 'str_sum': str_sum,
#                                  'children': [{'str_page': i, 'str_sum': str_sum}]}
#             # print(str_sum)
#
#
#     row_content = ''
#     for table in tables[:]:
#         for i, row in enumerate(table.rows[:]):  # 读每行
#             for cell in row.cells[:]:  # 读一行中的所有单元格
#                 c = cell.text
#                 row_content += c
#     for t in a:
#         t_count = row_content.count(t)
#         if t_count:
#             if d_a.get(t, False):
#                 d_a[t]['str_sum'] += t_count
#                 d_a[t]['str_page'] += f'、表格'
#                 d_a[t]['children'] += [{'str_page': '表格', 'str_sum': t_count}]
#             else:
#                 d_a[t] = {'str_page': '表格', 'str_sum': t_count,
#                           'children': [{'str_page': '表格', 'str_sum': t_count}]}
#     # print(row_content)
#
#     print(datetime.now() - s_time)
#     return d_a
#         #     d_a[t]['0'] += str_sum
#         #     d_a[t].append('sdsafsa')
#         # # content = document.paragraphs[i].text
#         # # 段落
#         #
#         #     if t in content:
#         #         str_sum = str(content).count(t)  # 每一页字符出现的次数
#         #         # print(d_a[t][0])
#         #         d_a[t][0] += 1
#         #         d_a[t].append('sdsafsa')
#         #         qwq = dict(sorted(d_a.items(), key=lambda qwq: qwq[1][0], reverse=True))
#         #         qwq1 = {k: v for k, v in qwq.items() if v[0] != 0}
#         #         # print(d_a[t])
#                 # print(qwq1)
#                 # d_a[t].append("第" + str(i) + "段的内容是：" + content)
#
#     # 表格
#     row_content = ''
#     for table in tables[:]:
#         for i, row in enumerate(table.rows[:]):  # 读每行
#             for cell in row.cells[:]:  # 读一行中的所有单元格
#                 c = cell.text
#                 row_content += c
#     for t in a:
#         if row_content.count(t):
#             d_a[t][0] += 1
#             d_a[t].append("表格内容:" + t)
#
#
#     qwq = dict(sorted(d_a.items(), key=lambda qwq: qwq[1][0], reverse=True))
#     qwq1 = {k: v for k, v in qwq.items() if v[0] != 0}
#     # print(qwq)
#     print(qwq1)
#
#     print(datetime.now() - s_time)
#     # print(extract_content)
#
# extract_content_docx('79.docx')
# def extract_content(pdf_path):
#     ee_time = datetime.now()
#     d_data ={}
#     # 内容提取，使用 pdfplumber 打开 PDF，用于提取文本
#     with pdfplumber.open(pdf_path) as pdf_file:
#         # 使用 PyPDF2 打开 PDF 用于提取图片
#         pdf_image_reader = PyPDF2.PdfFileReader(open(pdf_path, "rb"))
#         d_data['sum_page'] = pdf_image_reader.getNumPages()    # 获取总页数
#
#
#         # len(pdf.pages)为PDF文档页数，一页页解析
#         for i in range(len(pdf_file.pages)):
#
#             page_text = pdf_file.pages[i]
#             # page.extract_text()函数即读取文本内容
#             page_content = page_text.extract_text()
#             for j in a:
#                 str_sum = str(page_content).count(j)     # 每一页字符出现的次数
#
#                 if str_sum:
#                     if d_data.get(j,False):
#                         d_data[j]['str_sum'] += str_sum
#                         d_data[j]['str_page'].append(i)
#                     else:
#                         d_data[j] = {'str_sum': str_sum, 'str_page': [i]}
#
#     print("ee:",datetime.now()-ee_time)
#     print(d_data)
#
# # extract_content('智博会展商手册.pdf')
#
#
#
#
# # def extract_content(pdf_path):
# #
# #     d_data = {}
# #
# #     p_time = datetime.now()
# #     # 内容提取，使用 pdfplumber 打开 PDF，用于提取文本
# #     with pdfplumber.open(pdf_path) as pdf_file:
# #         # 使用 PyPDF2 打开 PDF 用于提取图片
# #         pdf_image_reader = PyPDF2.PdfFileReader(open(pdf_path, "rb"))
# #
# #         d_data['sum_page'] = pdf_image_reader.getNumPages()    # 获取总页数
# #         print("pdf_image_reader.getNumPages():", pdf_image_reader.getNumPages())
# #
# #         # print(d_data)
# #         print(pdf_image_reader.getNumPages())
# #         # print('pdf_file.pages:',pdf_file.pages)
# #         def qwq(t):
# #             print("pdf_file:", pdf_file)
# #             j_time = datetime.now()
# #
# #             # with pdfplumber.open(pdf_path) as pdf_file:
# #                 # print(pdf_image_reader.getNumPages())
# #
# #
# #             page_text = pdf_file.pages[t]
# #
# #             # page.extract_text()函数即读取文本内容
# #             page_content = page_text.extract_text()
# #             # print(page_content)
# #             for j in a:
# #
# #                 str_sum = str(page_content).count(j)  # 每一页字符出现的次数
# #                 # print(str_sum)
# #
# #                 if str_sum:
# #                     # print(d_data)
# #
# #                     if d_data.get(j, False):
# #                         with look:
# #                         #     print('**********')
# #                             d_data[j]['str_sum'] += str_sum
# #                             d_data[j]['str_page'].append(t)
# #                     else:
# #                         with look:
# #                         # print('++++++++++++++')
# #                             d_data[j] = {'str_sum': str_sum, 'str_page': [t]}
# #             pdf_file.close()
# #             print(d_data)
# #             print("datetime.now()- j_time:",datetime.now() - j_time)
# #
# #         import time, threading
# #         # pool = Pool(81)
# #         for i in range(81):
# #             t = threading.Thread(target=qwq,args=(i,))
# #             t.start()
# #
# #         # page_text_list = pool.map(qwq, range(len(pdf_file.pages)))  # 异步请求
# #         # qwq(4)
# #
# #
# #     print("datetime.now()-p_time:",datetime.now()-p_time)
# #     print(d_data)
#
#
# # extract_content('智博会展商手册.pdf')