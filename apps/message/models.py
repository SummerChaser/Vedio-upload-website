# _*_coding:utf-8_*_
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class  UsrInfo(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"用户名")
    email = models.EmailField(verbose_name=u"邮箱")
    address = models.CharField(max_length=100, verbose_name=u"地址")
    message = models.CharField(max_length=1000, verbose_name=u"留言信息")

    class Meta:
        verbose_name=u"用户留言信息"