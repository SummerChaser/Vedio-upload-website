# _*_ coding: utf-8 _*_

import xadmin

from .models import EmailVerifyRecord,Banner
from xadmin import views

class BaseSetting (object) :
    enable_themes = True
    use_bootswatch = True
xadmin.site.register(views.BaseAdminView,BaseSetting)

class GlobalSettings(object) :
    site_title = "超酷的后台"
    site_footer = "这里是一只想吃秋刀鱼的喵做的假的网站"
    # menu_style = "accordion"
xadmin.site.register(views.CommAdminView,GlobalSettings)

class EmailVerifyRecordAdmin(object) :
    list_display = ['code','email','send_type','send_time']
    search_fields = ['code','email','send_type']
    list_filter = ['code','email','send_type','send_time']

xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)


class BannerAdmin(object) :
    list_display = ['image', 'title', 'url', 'index','add_time']
    search_fields = ['image', 'title', 'url', 'index']
    list_filter = ['image', 'title', 'url', 'index','add_time']

xadmin.site.register(Banner,BannerAdmin)