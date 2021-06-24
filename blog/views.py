import logging

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .exception.blog_exception import UnSupportMethodException
from .models import *
from .response.rest_response import RestResponse
from .serializers import ConstantSerializer

logger = logging.getLogger(__name__)


# Create your views here.

class ConstantViewSet(viewsets.ModelViewSet):
    queryset = Constant.objects.all()
    serializer_class = ConstantSerializer


def index(request):
    return render(request=request, template_name='blog/index.html')


def list_category(request):
    logger.info('----- list_category -----')
    category = Category.objects.all()
    context = {
        'context': category
    }
    logger.info(context)
    return render(request=request, template_name='blog/list.html', context=context)


def list_constant_response(request):
    if request.method == 'GET':
        constant = Constant.objects.all()
        serializer = ConstantSerializer(constant, many=True)
        return RestResponse(serializer.data)
    raise UnSupportMethodException('不支持的HTTP请求')


@api_view(['GET', 'POST'])
def list_constant(request):
    if request.method == 'GET':
        constant = Constant.objects.all()
        serializer = ConstantSerializer(constant, many=True)
        return Response(serializer.data)
    raise UnSupportMethodException('不支持的HTTP请求')
