# _*_ coding: utf-8 _*_
from __future__ import unicode_literals

from django.db import models

from datetime import datetime

# Create your models here.

class Course(models.Model) :
    name = models.CharField(max_length=100,verbose_name=u"课程名称")
    decr = models.CharField(max_length=1000,verbose_name=u"课程描述")
    detail = models.TextField(verbose_name=u"课程详情")
    degree = models.CharField(max_length=4,choices=(("cj",u"初级"),("zj", u"中级"),("gj", u"高级")))
    learn_times = models.IntegerField(default=0,verbose_name=u"学习时长（分钟数）")
    students = models.IntegerField(default=0,verbose_name=u"学习人数")
    fav_nums = models.IntegerField(default=0,verbose_name=u"收藏人数")
    image = models.ImageField(max_length=100,upload_to="courses/%Y/%m",verbose_name=u"封面图")
    click_nums = models.IntegerField(default=0,verbose_name=u"点击数")
    add_time = models.DateField(default=datetime.now,verbose_name=u"添加时间")

    class Meta :
        verbose_name = u"课程"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

class Lesson (models.Model) :
    course = models.ForeignKey(Course,verbose_name=u"课程")
    name = models.CharField(max_length=100,verbose_name=u"章节名")
    add_time = models.DateField(default=datetime.now,verbose_name=u"添加时间")

    class Meta :
        verbose_name = u"章节"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name



class Vedio (models.Model) :
    lesson = models.ForeignKey(Lesson,verbose_name=u"章节")
    name = models.CharField(max_length=100, verbose_name = u"视频名")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta :
        verbose_name = u"视频"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name



class CourseResource (models.Model) :
    course = models.ForeignKey(Course,verbose_name=u"课程")
    name = models.CharField(max_length=100, verbose_name=u"资源名")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")
    download = models.FileField(max_length=100,upload_to="course/resource/%Y/%m",verbose_name=u"资源文件")

    class Meta :
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name













