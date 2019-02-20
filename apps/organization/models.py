# _*_ coding: utf-8 _*_

from __future__ import unicode_literals

from django.db import models

from datetime import datetime
# Create your models here.

class City (models.Model) :
    name = models.CharField(max_length=20, verbose_name=u"城市名称")
    desc = models.CharField(max_length=200,verbose_name=u"城市描述")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta :
        verbose_name = u"城市"
        verbose_name_plural = verbose_name

class CourseOrg (models.Model) :
    name = models.CharField(max_length=100,verbose_name=u"机构名称")
    desc = models.TextField(verbose_name=u"机构描述")
    click_nums = models.IntegerField(default=0,verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏数")
    image = models.ImageField(max_length=100, upload_to="org/%Y/%m", verbose_name=u"封面图")
    address = models.CharField(max_length=150,verbose_name=u"机构地址")
    city = models.ForeignKey(City,verbose_name=u"所在城市")
    add_time = models.DateField(default=datetime.now,verbose_name=u"添加时间")

    class Meta :
        verbose_name = u"课程机构"
        verbose_name_plural = verbose_name


class Teacher (models.Model) :
    org = models.ForeignKey(CourseOrg,verbose_name=u"所属机构 ")
    name = models.CharField(max_length=100, verbose_name=u"教师名称")
    work_years = models.IntegerField(default=0,verbose_name=u"工作年限")
    work_company = models.CharField(max_length=100,verbose_name=u"就职公司")
    work_position = models.CharField(max_length=100, verbose_name=u"公司职位")
    points = models.CharField(max_length=100, verbose_name=u"教学特点")
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏数")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta :
        verbose_name = u"教师"
        verbose_name_plural = verbose_name







