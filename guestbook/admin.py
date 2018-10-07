from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    """留言消息管理
    """

    list_display = ('name', 'email', 'active', 'posted') #后台管理呈现字段
    list_filter = ('active', 'posted') #留言过滤条件 时间/有效性
    search_fields = ('name', 'message') #留言消息搜索
    ordering      = ('-posted',) #时间呈现方式以倒序显现

#注册留言管理
admin.site.register(Message, MessageAdmin)
