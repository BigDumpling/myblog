from django.test import TestCase

from .models import Category


# Create your tests here.

class CategoryTest(TestCase):

    def test_list(self):
        print('开始测试')
        category = Category.objects.all()
        print(category)
