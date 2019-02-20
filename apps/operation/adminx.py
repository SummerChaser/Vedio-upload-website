# _*_ coding: utf-8 _*_

import xadmin

from .models import UserAsk,CourseComments,UserFavorite,UserMessage,UserCourse

class UserAskAdmin(object) :
    list_display = ['name', 'phone', 'course_name','add_time']
    search_fields = ['name', 'phone', 'course_name']
    list_filter = ['name', 'phone', 'course_name','add_time']

xadmin.site.register(UserAsk,UserAskAdmin)

class CourseCommentsAdmim(object) :
    list_display = ['user', 'course', 'comments', 'add_time']
    search_fields = ['user', 'course', 'comments']
    list_filter = ['user', 'course', 'comments', 'add_time']
xadmin.site.register(CourseComments,CourseCommentsAdmim)


class UserFavoriteAdmim(object) :
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']
xadmin.site.register(UserFavorite,UserFavoriteAdmim)

class UserMessageAdmim(object) :
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields =  ['user', 'message', 'has_read']
    list_filter =  ['user', 'message', 'has_read', 'add_time']
xadmin.site.register(UserMessage,UserMessageAdmim)

class UserCourseAdmim(object) :
    list_display = ['user', 'course', 'add_time']
    search_fields =['user', 'course']
    list_filter = ['user', 'course', 'add_time']
xadmin.site.register(UserCourse,UserCourseAdmim)
