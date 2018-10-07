from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Message 

# Create your views here.

def post_message(request):
    """首页留言提交处理
    """
    #如果用户客户端提交方法是POST
    if request.method =='POST':
        # 得到想要的数据项
        name = request.POST.get('name', '')
        email = request.POST.get('email','')
        content = request.POST.get('message','')
        # 保障name和content为必填
        if name and content:
            #创建message实例
            msg = Message(name=name, email=email, message=content)
            # 留言保存
            msg.save()
            #留言填写后转跳到首页
            return redirect(reverse('home'))
        else:
            return HttpResponse('用户名及留言必须填写!')
    return redirect(reverse('home'))
