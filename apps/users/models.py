# _*_ coding: utf-8 _*_

from __future__ import unicode_literals

#引入datime 验证码过期验证使用
from datetime import datetime


from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserProfile (AbstractUser) :
    nick_name = models.CharField(max_length=50,verbose_name=u"昵称",default="")
    birthday = models.DateField(verbose_name=u"生日",null=True,blank=True)
    gender = models.CharField(max_length=5,choices=( ("man",u"男"),("femal",u"女") ),default="man" ,verbose_name=u"性别")
    address = models.CharField(max_length=100,default=u"",verbose_name=u"地址")
    mobile = models.CharField(max_length=11,null=True,blank=True,verbose_name=u"电话")
    image = models.ImageField(max_length=100,upload_to="image/%Y/%m",default=u"image/default.png",verbose_name=u"头像")

    class Meta :
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username

class EmailVerifyRecord (models.Model) :
    code = models.CharField(max_length=20,verbose_name=u"验证码")
    email = models.EmailField(max_length=50,verbose_name=u"邮箱")
    send_type = models.CharField(max_length=10,choices=(("register",u"注册"),("forget",u"找回密码")))
    send_time = models.DateField(default=datetime.now)

    class Meta :
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return "{0} ({1})".format(self.code,self.email)

class Banner (models.Model) :
    image = models.ImageField(max_length=100,upload_to="banner/%Y/%m",verbose_name=u"轮播图")
    title = models.CharField(max_length=50,verbose_name=u"标题")
    url = models.URLField(max_length=100,verbose_name=u"访问地址")
    index = models.IntegerField(default=100,verbose_name=u"顺序")
    add_time = models.DateField(default=datetime.now,verbose_name=u"添加时间")

    class Meta :
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name










