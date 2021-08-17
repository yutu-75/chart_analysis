


from pathlib import Path
import os
p = Path(r'C:\Users\lixin_data\Desktop\chart_analysis\chart_analysis\apps\home\static\ciyun_templates')
# img_list = p.iterdir()
img_list = os.listdir(p)
print(p.joinpath('1sss.png'))
# print(img_list)
# print(list(img_list))

# for child in p.iterdir():
    # print(child)

# for i in img_list:
    # print(i)
# print(list(img_list))