# a = [i for i in range(30)]
# print(a)

a = ['1']

b = ['2','3']
a.append(*b)
print(a)


from docx import Document
from datetime import datetime, timedelta
import uuid
from multiprocessing.dummy import Pool  # 线程池
from multiprocessing import Process,Lock
look = Lock() #创建锁
print(uuid.uuid1())
from threading import Thread

import PyPDF2
import pdfplumber
def qq():
    s = datetime.now()
    def qwq(a):
        print(a)
        # with pdfplumber.open('智博会展商手册.pdf') as pdf_file:
        #     print(pdf_file)
    pool = Pool(81)
    page_text_list = pool.map(qwq, range(81))  # 异步请求
    print(datetime.now()-s)
    # qwq(4)
qq()
