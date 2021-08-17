from django.db import models

# Create your models here.


class File(models.Model):
    name = models.CharField(max_length=50)
    date1 = models.DateTimeField(auto_now=True, null=True)
    date2 = models.DateTimeField(auto_now_add=True, null=True)
    file = models.ImageField(upload_to='file', null=True)  # 写上upload_to，后面指定一个路径，那么将来上传的文件会直接生成到配置文件中的那个medias文件夹中的img文件夹中，不需要我们自己写读取文件内容写入本地文件的操作，django内部帮我们自动处理了