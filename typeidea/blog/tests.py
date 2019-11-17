from django.test import TestCase, Client

# Create your tests here.
from blog.models import Post, Category, Tag
from django.contrib.auth.models import User


class BlogTestCase(TestCase):
    # def setUp(self):
    #     Category.objects.create(
    #         name='测试分类',
    #         owner='作者'
    #     )
    #     Tag.objects.create(
    #         name='测试标签',
    #         owner='作者'
    #     )
    #     Post.objects.create(
    #         title='标题',
    #         description='摘要',
    #         content='content',
    #         content_html='content_html',
    #         status=Post.STATUS_NORMAL,
    #         category='测试分类',
    #         tags='测试标签',
    #         owner='作者',
    #         is_md=True,
    #     )

    def test_get_index(self):
        # 测试首页的可用性
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200, 'status code must be 200!')

    def test_get_autocomplete_category(self):
        # 测试首页的可用性
        client = Client()
        response = client.get('/category-autocomplete/?q=py')
        self.assertEqual(response.status_code, 200, 'status code must be 200!')

    def test_get_autocomplete_tag(self):
        # 测试首页的可用性
        client = Client()
        response = client.get('/tag-autocomplete/?q=py')
        self.assertEqual(response.status_code, 200, 'status code must be 200!')
