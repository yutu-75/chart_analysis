"""chart_analysis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('user/', include("home.urls")),
    path("", views.index),
    path("datatable/", views.datatable),
    path("datatable1/", views.datatable1),
    path("chart_table/", views.chart_table),
    path("show_chart/", views.show_chart),
    path('word_count/', views.word_count),
    path("choice_database/", views.choice_database),

    # re_path(r'datatable/<int:f_sum>/', views.datatable,),
]

