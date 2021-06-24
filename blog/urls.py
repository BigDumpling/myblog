from django.urls import path, include
from rest_framework import routers

from .views import *

app_name = 'blog'

router = routers.DefaultRouter()
router.register(r'constant', ConstantViewSet)

urlpatterns = [
    path('', index),
    path('category/list', list_category),
    path('constant/list/rest', list_constant_response),
    path('constant/list', list_constant),
    path('rest/', include(router.urls)),
]
