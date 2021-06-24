import logging

from django.http.response import HttpResponse
from rest_framework.renderers import JSONRenderer

logger = logging.getLogger(__name__)


class RestResponse(HttpResponse):
    """
    自定义Rest响应，返回JSON格式数据
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(RestResponse, self).__init__(content, **kwargs)
