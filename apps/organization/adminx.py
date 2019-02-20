# _*_ coding: utf-8 _*_

import xadmin
from .models import CourseOrg,City,Teacher

class CityAdmin(object) :
    list_display = ['name', 'desc','add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc','add_time']
xadmin.site.register(City,CityAdmin)


class CourseOrgAdmin(object) :
    list_display = ['name', 'desc', 'click_nums', 'fav_nums','image','address','city','add_time']
    search_fields = ['name', 'desc', 'click_nums', 'fav_nums','image','address','city']
    list_filter = ['name', 'desc', 'click_nums', 'fav_nums','image','address','city','add_time']
xadmin.site.register(CourseOrg,CourseOrgAdmin)


class TeacherAdmin(object) :
    list_display = ['org', 'name', 'work_years', 'work_company','work_position','points','click_nums','fav_nums','add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company','work_position','points','click_nums','fav_nums']
    list_filter = ['org', 'name', 'work_years', 'work_company','work_position','points','click_nums','fav_nums','add_time']
xadmin.site.register(Teacher,TeacherAdmin)