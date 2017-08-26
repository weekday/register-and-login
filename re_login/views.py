#coding:utf-8
from django.shortcuts import render,render_to_response
import hashlib
from models import Register
from django.http import HttpResponse
from django.template import RequestContext
from form import UserLogin,UserRegister

# Create your views here.
def take_md5(content):
    hash = hashlib.md5()    #创建hash加密实例
    hash.update(content)    #hash加密
    result = hash.hexdigest()  #得到加密结果
    return result

def register(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid(): #获取表单信息
            username = form.cleaned_data['username']
            namefilter = Register.objects.filter(username = username)
            if len(namefilter) > 0:
                return render_to_response('register.html',{'error':'用户名已存在'},context_instance=RequestContext(request))
            else:
                password1 = form.cleaned_data['password1']
                password2 = form.cleaned_data['password2']
                if password1 != password2:
                    return render_to_response('register.html',{'error':'两次输入的密码不一致！'},context_instance=RequestContext(request))
                else:
                    password = take_md5(password1)
                    email = form.cleaned_data['email']
                    phone_number = form.cleaned_data['phone_number']
                    #将表单写入数据库
                    user = Register.objects.create(username=username,password=password,email=email,phone_number=phone_number)
                    user.save()
                    return render_to_response('success.html',{'username':username,'operation':'注册'},context_instance=RequestContext(request))
    else:
        form = UserRegister()
        return render_to_response('register.html',{'form':form},context_instance=RequestContext(request))

def login(request):
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid(): #获取表单信息
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password = take_md5(password)
            namefilter = Register.objects.filter(username=username,password=password)
            if len(namefilter) > 0:
                return render_to_response('success.html',{'username':username,'operation':'登录'},context_instance=RequestContext(request))
            else:
                return render_to_response('login.html',{'error':'该用户名不存在！'},context_instance=RequestContext(request))
    else:
        form =UserLogin()
        return render_to_response('login.html',{'form':form},context_instance=RequestContext(request))