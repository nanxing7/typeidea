import xadmin
from django.urls import reverse
from django.utils.html import format_html
from xadmin.layout import Fieldset, Row, Container
from xadmin.filters import manager
from xadmin.filters import RelatedFieldListFilter

from blog.adminforms import PostAdminForm
from typeidea.base_admin import BaseOwnerAdmin
from .models import Post, Category, Tag


# Register your models here.

class PostInline:
    """内链"""
    form_layout = (
        Container(
            Row('title', 'desc')
        )
    )
    extra = 1  # 控制额外多几个
    model = Post


@xadmin.sites.register(Category)
class CategoryAdmin(BaseOwnerAdmin):
    inlines = [PostInline, ]
    list_display = ('name', 'status', 'is_nav', 'created_time', 'post_count')
    fields = ('name', 'status', 'is_nav')

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'


@xadmin.sites.register(Tag)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'created_time', 'post_count',)
    fields = ('name', 'status',)

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'


# class CategoryOwnerFilter(RelatedFieldListFilter):
#     """自定义过滤器只展示当前用户分类"""
#
#     title = '分类过滤器'
#     parameter_name = 'owner_category'
#
#     def lookups(self, request, model_admin):
#         return Category.objects.filter(owner=request.user).values_list('id', 'name')
#
#     def queryset(self, request, queryset):
#         category_id = self.value()
#         if category_id:
#             return queryset.filter(category_id=self.value())
#         return queryset


class CategoryOwnerFilter(RelatedFieldListFilter):
    """自定义过滤器"""

    @classmethod
    def test(cls, field, request, params, model, admin_view, field_path):
        """确认字段是否需要被当前的过滤器处理"""
        return field.name == 'category'

    def __init__(self, field, request, params, model, model_admin, field_path):
        super().__init__(field, request, params, model, model_admin, field_path)  # 执行父类 __init__ 方法
        # 重新获取lookup_choices，根据owner过滤
        self.lookup_choices = Category.objects.filter(owner=request.user).values_list('id', 'name')


manager.register(CategoryOwnerFilter, take_priority=True)  # 注册到过滤器管理器中


@xadmin.sites.register(Post)
class PostAdmin(BaseOwnerAdmin):
    """定制的文章发表界面"""
    list_display = [
        'title', 'category', 'status',
        'created_time', 'owner', 'operator',
    ]
    list_display_links = []
    exclude = ['owner']
    list_filter = ['category', ]
    search_fields = ['title', 'category__name']

    actions_on_top = True
    actions_on_bottom = True

    form = PostAdminForm

    # 编辑页面

    save_on_top = True

    form_layout = (
        Fieldset(
            '基础信息',
            Row("title", "category"),
            'status',
            'tag',
        ),
        Fieldset(
            '内容信息',
            'desc',
            'is_md',
            'content_ck',
            'content_md',
            'content',
        )
    )

    def operator(self, obj):
        """自定义"""
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('xadmin:blog_post_change', args=(obj.id,)),
        )

    operator.short_description = '操作'

    class Media:
        css = {
            'all': ()
        }
        js = ()

# @xadmin.sites.register(Post)
# class PostAdmin(BaseOwnerAdmin):
#     form = PostAdminForm
#     list_display = [
#         'title', 'category', 'status',
#         'created_time', 'owner', 'operator'
#     ]
#     list_display_links = []
#
#     list_filter = ['category', ]
#     search_fields = ['title', 'category__name']
#     save_on_top = True
#
#     actions_on_top = True
#     actions_on_bottom = True
#
#     # 编辑页面
#     save_on_top = True
#
#     exclude = ['owner']
#     form_layout = (
#         Fieldset(
#             '基础信息',
#             Row("title", "category"),
#             'status',
#             'tag',
#         ),
#         Fieldset(
#             '内容信息',
#             'desc',
#             'is_md',
#             'content_ck',
#             'content_md',
#             'content',
#         )
#     )
#
#     def operator(self, obj):
#         return format_html(
#             '<a href="{}">编辑</a>',
#             reverse('xadmin:blog_post_change', args=(obj.id,))
#         )
#
#     operator.short_description = '操作'
