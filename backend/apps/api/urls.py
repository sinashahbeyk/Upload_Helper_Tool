from django.urls import path
from .views import *

urlpatterns = [
    path('', ArticleList.as_view(), name='articles'),
    path('create/', ArticleCreate.as_view(), name='article-create'),
    path('update/<int:pk>', ArticleUpdate.as_view(), name='article-update'),
    path('delete/<int:pk>', ArticleDelete.as_view(), name='article-delete'),

    path('user/', UserList.as_view(), name='users'),

]
