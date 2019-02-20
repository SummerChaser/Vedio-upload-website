# _*_ coding: utf-8 _*_
import xadmin
from .models import Course,CourseResource,Lesson,Vedio

class CourseAdmin (object) :

    list_display = ['name', 'decr','detail','degree','learn_times','students','fav_nums','image','click_nums','add_time']
    search_fields =  ['name', 'decr','detail','degree','learn_times','students','fav_nums','image','click_nums']
    list_filter =  ['name', 'decr','detail','degree','learn_times','students','fav_nums','image','click_nums','add_time']
xadmin.site.register(Course,CourseAdmin)


class CourseResourceAdmin(object) :
    list_display = ['course', 'name', 'add_time','download']
    search_fields = ['course', 'name','download']
    list_filter = ['course', 'name', 'add_time','download']

xadmin.site.register(CourseResource,CourseResourceAdmin)


class LessonAdmin(object) :
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course', 'name', 'add_time']

xadmin.site.register(Lesson,LessonAdmin)


class VedioAdmin(object) :
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']
xadmin.site.register(Vedio,VedioAdmin)