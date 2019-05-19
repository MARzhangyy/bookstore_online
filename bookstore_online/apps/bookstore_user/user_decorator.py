# coding=utf-8
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


# 如果未登录则转到登录页面
def login(func):
    def login_fun(request, *args, **kwargs):
        if 'user_id' in request.session:
            return func(request, *args, **kwargs)
        else:
            red = HttpResponseRedirect(reverse("bookstore_user:login"))
            red.set_cookie('url', request.get_full_path())
            # 保证用户再登录验证之后仍点击到希望的页面
            return red
    return login_fun
