from django.contrib import admin


class BaseOwnerAdmin(admin.ModelAdmin):
    """
    1. 用来自动补充文章、分类、标签、侧边栏、友链这些 Model 的 owner 字段
    2. 用来针对 queryset 过滤当前用户的数据
    """

    exclude = ('owner',)

    def get_queryset(self, request):
        """重写方法，返回当前用户的内容"""
        qs = super(BaseOwnerAdmin, self).get_queryset(request)  # 执行父类方法，获取 request
        return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        """重写方法，返回当前用户的内容"""
        obj.owner = request.user
        super().save_model(request, obj, form, change)
