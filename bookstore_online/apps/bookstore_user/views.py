#coding=utf-8
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from django.http import JsonResponse
#hashlib加密算法
from hashlib import sha1

from .models import BooksBrowser,UserInfo
from . import user_decorator
from bookstore_order.models import *


def register(request):

    context = {
        'title': '用户注册',
    }
    return render(request, 'bookstore_user/register.html', context)


def register_handle(request):
    #后台获取从前端表单中传过来的数据
    username = request.POST.get('user_name')
    password = request.POST.get('pwd')
    confirm_pwd = request.POST.get('confirm_pwd')
    email = request.POST.get('email')

    # 判断两次密码一致性
    if password != confirm_pwd:
        return redirect('/user/register/')
    '''
    密码加密
    '''
    #sha1加密算法，生成hash对象
    s1 = sha1()
    #调用update方法会在前面加密的基础上更新加密
    s1.update(password.encode('utf8'))
    #生成加密后的十六进制结果
    encrypted_pwd = s1.hexdigest()

    # 创建对象ORM中的create方法可快速将数据存到数据库中
    UserInfo.objects.create(uname=username, upwd=encrypted_pwd, uemail=email)
    # 注册成功
    context = {
        'title': '用户登录',
        'username': username,
    }
    return render(request, 'bookstore_user/login.html', context)


def register_exist(request):
    username = request.GET.get('uname')
    count = UserInfo.objects.filter(uname=username).count()
    return JsonResponse({'count': count})


def login(request):
    uname = request.COOKIES.get('uname', '')
    context = {
        'title': '用户登录',
        'error_name': 0,
        'error_pwd': 0,
        'uname': uname,
    }
    return render(request, 'bookstore_user/login.html', context)


def login_handle(request):
    # 接受请求信息
    uname = request.POST.get('username')
    upwd = request.POST.get('pwd')
    remenber = request.POST.get('remenber', 0)
    users = UserInfo.objects.filter(uname=uname)
    if len(users) == 1:  # 判断用户密码并跳转
        s1 = sha1()
        s1.update(upwd.encode('utf8'))
        if s1.hexdigest() == users[0].upwd:
            url = request.COOKIES.get('url', '/')
            # 继承与HttpResponse 在跳转的同时 设置一个cookie值
            red = HttpResponseRedirect(url)
            # 是否勾选记住用户名，设置cookie
            if remenber != 0:
                red.set_cookie('uname', uname)
            else:
                red.set_cookie('uname', '', max_age=-1)  # 设置过期cookie时间，立刻过期
            request.session['user_id'] = users[0].id
            request.session['user_name'] = uname
            return red
        else:
            context = {
                'title': '用户名登录',
                'error_name': 0,
                'error_pwd': 1,
                'uname': uname,
                'upwd': upwd,
            }
            return render(request, 'bookstore_user/login.html', context)
    else:
        context = {
            'title': '用户名登录',
            'error_name': 1,
            'error_pwd': 0,
            'uname': uname,
            'upwd': upwd,
        }
        return render(request, 'bookstore_user/login.html', context)


def logout(request):  # 用户登出
    request.session.flush()  # 清空当前用户所有session
    return redirect(reverse("bookstore_goods:index"))


@user_decorator.login
def info(request):  # 用户中心
    username = request.session.get('user_name')
    user = UserInfo.objects.filter(uname=username).first()
    browser_goods = BooksBrowser.objects.filter(user=user).order_by("-browser_time")
    goods_list = []
    if browser_goods:
        goods_list = [browser_good.good for browser_good in browser_goods]  # 从浏览商品记录中取出浏览商品
        explain = '最近浏览'
    else:
        explain = '无浏览记录'

    context = {
        'title': '用户中心',
        'page_name': 1,
        'user_contact': user.ucontact,
        'user_address': user.uaddress,
        'user_name': username,
        'goods_list': goods_list,
        'explain': explain,
    }
    return render(request, 'bookstore_user/user_center_info.html', context)


@user_decorator.login
def order(request, index):
    user_id = request.session['user_id']
    orders_list = OrderInfo.objects.filter(user_id=int(user_id)).order_by('-ordertime')
    paginator = Paginator(orders_list, 2)
    page = paginator.page(int(index))
    context = {
        'paginator': paginator,
        'page': page,
        'title': "用户中心",
        'page_name': 1,
    }
    return render(request, 'bookstore_user/user_center_order.html', context)


@user_decorator.login
def site(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    if request.method == "POST":
        user.urecieve = request.POST.get('urecieve')
        user.uaddress = request.POST.get('uaddress')
        user.zipcode = request.POST.get('zipcode')
        user.ucontact = request.POST.get('ucontact')
        user.save()
    context = {
        'page_name': 1,
        'title': '用户中心',
        'user': user,
    }
    return render(request, 'bookstore_user/user_center_site.html', context)
