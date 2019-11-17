"""typeidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.contrib.sitemaps import views as sitemap_views
from rest_framework.routers import DefaultRouter
import xadmin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from blog.views import CategoryView, PostDetailView, IndexView, TagView, SearchView, AuthorView
from comment.views import CommentView
from config.views import LinkListView
from blog.apis import PostViewSet
from .autocomplete import CategoryAutocomplete, TagAutocomplete
from blog.rss import LatestPostFeed
from blog.sitemap import PostSitemap

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'post', PostViewSet, base_name="api")
router.register(r'category', PostViewSet, base_name="api-category")

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('categories/<category_id>', CategoryView.as_view(), name='category-list'),
    path('tags/<tag_id>', TagView.as_view(), name='tag-list'),
    path('post/<post_id>.html', PostDetailView.as_view(), name='post-detail'),
    path('links/', LinkListView.as_view(), name='links'),
    path('search/', SearchView.as_view(), name='search'),
    path('author/<owner_id>', AuthorView.as_view(), name='author'),
    path('comment/', CommentView.as_view(), name="comment"),
    path('admin/', xadmin.site.urls, name='admin'),
    path('rss/', LatestPostFeed(), name='rss'),
    path('sitemap.xml', sitemap_views.sitemap, {'sitemaps': {'posts': PostSitemap}}),
    path("category-autocomplete/", CategoryAutocomplete.as_view(), name='category-autocomplete'),
    path("tag-autocomplete/", TagAutocomplete.as_view(), name='tag-autocomplete'),
    path('api/', include(router.urls), name="api"),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
