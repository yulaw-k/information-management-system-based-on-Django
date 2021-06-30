from django.urls import path
from .views import *

urlpatterns = [

    # 首页
    path('', indexView, name='index'),
    # 用户注册
    path('register.html', registerView, name='register'),
    # 用户登录
    path('login.html', loginView, name='login'),
    # 用户注销
    path('logout.html', logoutView, name='logout'),
    # 用户中心
    path('info.html', infoView, name='info'),
    # 信息管理模块
    path('infoManage.html', infoManageView, name='infoManage'),
    # 新增信息
    path('create.html', createView, name='create'),
    # 修改信息
    path('update.html', updateView, name='update'),
    # 删除信息
    path('delete.html', delInfoView, name='delete'),
    # 查询信息
    path('query.html', queryView, name='query'),

    # 日程安排模块
    path('schedule.html', scheduleView, name='schedule'),

    path('result', result, name='result'),
]