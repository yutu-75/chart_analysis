import json

from pyecharts.charts import BMap
from pyecharts import options as opts

"""
参考地址: https://gallery.echartsjs.com/editor.html?c=bmap-bus
"""

BAIDU_MAP_AK = "NbQaofPi6y8GnBkfd2cmr1RbhLytNhqj"

from pyecharts import options as opts
from pyecharts.charts import BMap
from pyecharts.faker import Faker

c = (
    BMap()
    .add_schema(baidu_ak="FAKE_AK", center=[120.13066322374, 30.240018034923])
    .add(
        "bmap",
        [list(z) for z in zip(Faker.provinces, Faker.values())],
        label_opts=opts.LabelOpts(formatter="{b}"),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="BMap-基本示例"))
    .render("bmap_base.html")
)