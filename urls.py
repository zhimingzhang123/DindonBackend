"""
URL(Uniform Resource Locator, 统一资源定位符)是对可以从互联网上得到的资源位置和访问方法的一种简洁表示,
是互联网上标准资源的地址.
互联网上的每个文件都有一个唯一的URL,用于指出文件的路径位置.
简单的说,URL就是常说的网址,每个地址代表不同的网页,在Django中,URL也称为URLconf

"""

# 根目录的urls.py
# 在App里添加urls.py是将属于App的URL都写入到该文件中,而项目根目录的urls.py是将每个App的urls.py统一管理
# 当程序收到用户请求的时候,首先在根目录的urls.py查找该URL是属于哪个App,然后再从App的urls.py找到具体的URL信息

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 此处代码设定了两个URL地址,分别是Admin站点管理和首页地址
    path('admin/', admin.site.urls),
    path('', include('index.urls'))
]
