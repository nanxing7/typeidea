from django.contrib import admin

from typeidea.base_admin import BaseOwnerAdmin

# Register your models here.
from .models import Comment


class CommentAdmin(BaseOwnerAdmin):
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')
