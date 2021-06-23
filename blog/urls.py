from django.urls import path

from .views import *

app_name = 'blog'

urlpatterns = [
    path('', hello),
    path('category/list', list_category)
]
