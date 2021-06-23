import logging

from django.http import HttpResponse
from django.shortcuts import render

from .models import *

logger = logging.getLogger(__name__)


# Create your views here.

def hello(request):
    logger.info('----- hello -----')
    return HttpResponse('Hello World')


def list_category(request):
    logger.info('----- list_category -----')
    category = Category.objects.all()
    context = {
        'context': category
    }
    logger.info(context)
    return render(request=request, template_name='blog/list.html', context=context)
