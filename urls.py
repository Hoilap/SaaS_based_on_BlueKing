# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community
Edition) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""
'''
from django.contrib import admin
from django.urls import include, re_path

urlpatterns = [
    # 出于安全考虑，默认屏蔽admin访问路径。
    # 开启前请修改路径随机内容，降低被猜测命中几率，提升安全性
    # re_path(r'^admin_'{6个以上任意字符串}'/', admin.site.urls),
    # 如果你习惯使用 Django 模板，请在 bk_framework_app 里开发你的应用
    re_path(r"^", include("bk_framework_app.urls")),
    # 如果你通过drf来开发后端接口，请在 bk_framework_api 里开发你的应用
    re_path(r"^api/", include("bk_framework_api.urls")),
    re_path(r"^account/", include("blueapps.account.urls")),
    
    re_path(r"^i18n/", include("django.conf.urls.i18n")),
]
'''

from django.contrib import admin
from django.urls import path
from moments.views import home, show_user, show_status,submit_post,set_super_user,load_data,load_data2
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('user/', show_user),
    path('status/', show_status),
    path('post/', submit_post),
    path('set-su/', set_super_user),
    ## 配置路由规则
    path('add-su/',load_data),
    path('add-su2/',load_data2)
]