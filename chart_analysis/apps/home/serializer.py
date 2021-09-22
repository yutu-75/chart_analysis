from rest_framework import serializers
from .models import File
class FileSerializer(serializers.ModelSerializer):
    """序列化"""

    class Meta():
        model = File
        fields = ('name', 'file',)