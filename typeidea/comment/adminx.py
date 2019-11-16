import xadmin

from typeidea.base_admin import BaseOwnerAdmin

# Register your models here.
from .models import Comment


@xadmin.sites.register(Comment)
class CommentAdmin(BaseOwnerAdmin):
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')
