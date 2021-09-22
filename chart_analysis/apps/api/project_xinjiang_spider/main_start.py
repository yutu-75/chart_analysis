import json
from datetime import datetime
import pymysql
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chart_analysis.settings')
django.setup()
from chart_analysis.apps.api.models import File
a = File(name='qwq', file='qwq')
a.save()



