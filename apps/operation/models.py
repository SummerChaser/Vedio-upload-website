# _*_ coding: utf-8 _*_

from __future__ import unicode_literals

from django.db import models

from datetime import datetime

from users.models import UserProfile
from courses.models import Course

# Create your models here.

class UserAsk (models.Model) :
    name = models.CharField(max_length=20,verbose_name=u"姓名")
    phone = models.CharField(max_length=11,verbose_name=u"电话")
    course_name = models.CharField(max_length=50,verbose_name=u"课程名")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户咨询"
        verbose_name_plural = verbose_name


class CourseComments(models.Model) :
    user = models.ForeignKey(UserProfile,verbose_name=u"用户")
    course = models.ForeignKey(Course,verbose_name=u"课程")
    comments = models.CharField(max_length=500,verbose_name=u"评论")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程评论"
        verbose_name_plural = verbose_name

class UserFavorite(models.Model) :
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    fav_id = models.IntegerField(default=0,verbose_name=u"数据id")
    fav_type = models.IntegerField(default=1,choices=((1,u"课程"),(2,u"课程机构"),(3,u"讲师")),verbose_name=u"收藏类型")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程收藏"
        verbose_name_plural = verbose_name

class UserMessage(models.Model) :
    # 0为全员消息，否则为消息发送的用户id
    user = models.IntegerField(default=0,verbose_name=u"接收用户")
    message = models.CharField(max_length=500,verbose_name=u"消息内容")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")
    has_read = models.BooleanField(default=False,verbose_name=u"是否已读")

    class Meta:
        verbose_name = u"用户消息"
        verbose_name_plural = verbose_name

class UserCourse(models.Model) :
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    course = models.ForeignKey(Course, verbose_name=u"课程")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户课程"
        verbose_name_plural = verbose_name


















