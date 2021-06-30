from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from user.form import ScheduleForm
from user.models import PersonInfo, Schedule


def indexView(request):
    return render(request, 'index.html', locals())


# 使用表单实现用户注册
def registerView(request):
    userLogin = False
    if request.method == 'POST':
        user = UserCreationForm(request.POST)
        if user.is_valid():
            user = user.save(commit=False)
            user.email = request.POST.get('em')
            user.save()
            tips = '注册成功'
            return redirect(reverse('user:login'))
        else:
            tips = '注册失败'
    user = UserCreationForm()
    return render(request, 'user.html', locals())


# 用户登录
def loginView(request):
    tips = '请登录'
    userLogin = True
    if request.method == 'POST':
        u = request.POST.get('username', '')
        p = request.POST.get('password1', '')
        if User.objects.filter(username=u):
            user = authenticate(username=u, password=p)
            if user:
                if user.is_active:
                    # 登录当前账户
                    login(request, user)
                return redirect(reverse('user:info'))
            else:
                tips = '账号密码错误，请重新输入'
        else:
            tips = '用户不存在，请注册'
    user = UserCreationForm()
    return render(request, 'user.html', locals())


# 退出登录
def logoutView(request):
    logout(request)
    return redirect(reverse('user:index'))


# 用户中心
# login_required 判断用户是否已登录
@login_required(login_url='/login.html')
def infoView(request):
    return render(request, 'info.html', locals())


@login_required(login_url='/login.html')
def infoManageView(request):
    return render(request, 'infoManage.html', locals())


def result(request):
    return HttpResponse('Success')


@login_required(login_url='/login.html')
def createView(request):
    title = '学生信息新增模块'
    if request.method == 'POST':
        name = request.POST.get('name', '')
        major = request.POST.get('major', '')
        sex = request.POST.get('sex', '')
        number = request.POST.get('number', '')
        age = request.POST.get('age', '')
        address = request.POST.get('address', '')
        if all([name, major, sex, number, age, address]):
            d = dict(name=name, major=major, sex=sex, number=number, age=age, address=address)
            v = PersonInfo.objects.create(**d)
            tips = '新增 ' + str(v.name) + ' 信息成功！'
        else:
            tips = '所有选项为必填项！'
    return render(request, 'create.html', locals())


# 修改学生信息
@login_required(login_url='/login.html')
def updateView(request):
    title = '学生信息修改模块'
    if request.method == 'POST':
        name = request.POST.get('name', '')
        major = request.POST.get('major', '')
        sex = request.POST.get('sex', '')
        number = request.POST.get('number', '')
        age = request.POST.get('age', '')
        address = request.POST.get('address', '')
        if all([name, major, sex, number, age, address]):
            p = PersonInfo.objects.filter(name=name)
            if len(p):
                d = dict(name=name, major=major, sex=sex, number=number, age=age, address=address)
                PersonInfo.objects.filter(name=name).update(**d)
                tips = '修改 ' + str(p[0].name) + ' 信息成功！'
            else:
                tips = '修改失败，未找到该学生！'

        else:
            tips = '所有选项为必填项！'
    return render(request, 'update.html', locals())


# 删除学生信息
@login_required(login_url='/login.html')
def delInfoView(request):
    title = '学生信息删除模块'
    if request.method == 'POST':
        name = request.POST.get('name','')
        print('!'+name+'!')
        if name:
            summ = PersonInfo.objects.filter(name=name)
            num = len(list(summ))
            if num:
                summ.delete()
                # PersonInfo.objects.filter(name=name).delete()
                tips = '删除成功！共删除' + str(num) + '条数据！'
                return render(request, 'delete.html', locals())
            else:
                tips = "不存在该学生！"
        else:
            tips = "删除的名字不能为空!"
    return render(request, 'delete.html', locals())


# 查询学生信息
@login_required(login_url='/login.html')
def queryView(request):
    title = '学生信息查询模块'
    if request.method == 'POST':
        name = request.POST.get('name', '')
        if name:
            p = PersonInfo.objects.filter(name=name)
            num = len(list(p))
            print(num)
            if num == 0:
                tips = '未找到该学生信息！'
            return render(request, 'query.html', locals())
        else:
            tips = "查询的名字不能为空!"
            return render(request, 'query.html', locals())
    p = PersonInfo.objects.all()
    return render(request, 'query.html', locals())


@login_required(login_url='/login.html')
def scheduleView(request):
    if request.method == 'GET':
        v = ScheduleForm()
        p = Schedule.objects.filter(person_id=request.user.id)
        return render(request, 'schedule.html', locals())
    else:
        v = ScheduleForm(data=request.POST)
        v1 = v.save(commit=False)
        v1.person_id = request.user.id
        v1.save()
        tips = '新增日程成功！'
        p = Schedule.objects.filter(person_id=request.user.id)
        return render(request, 'schedule.html', locals())