from django.urls import path
from .views import ArticleList, ArticleDetail, UserList, UserDetail

app_name = 'apps.blog'

urlpatterns = [
    path('', ArticleList.as_view(), name='articles'),
    path('detail/<int:pk>', ArticleDetail.as_view(), name='article-detail'),
    path('user', UserList.as_view(), name='users'),
    path('user/<int:pk>', UserDetail.as_view(), name='user-detail'),
]
