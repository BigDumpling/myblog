from rest_framework import serializers

from .models import Constant


#
# class ConstantSerializer(serializers.HyperlinkedModelSerializer):
#     id = serializers.IntegerField(read_only=True)
#     status = serializers.IntegerField(default=1)
#     param_key = serializers.CharField(max_length=32, required=True)
#     param_name = serializers.CharField(max_length=64, required=True)
#     param_value = serializers.CharField(style={'base_template': 'textarea.html'}, max_length=256, required=True)
#     remark = serializers.CharField(max_length=256, required=False, allow_blank=True, allow_null=True)
#     create_time = serializers.DateTimeField(read_only=True)
#     modify_time = serializers.DateTimeField(read_only=True)
#
#     class Meta:
#         model = Constant
#         fields = ('id', 'status', 'param_key', 'param_name', 'param_value', 'remark', 'create_time', 'modify_time')


class ConstantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Constant
        fields = ('id', 'status', 'param_key', 'param_name', 'param_value', 'remark', 'create_time', 'modify_time')
