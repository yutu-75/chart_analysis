from rest_framework import serializers
from .models import File
class FileSerializer(serializers.ModelSerializer):
    """εΊεε"""

    class Meta():
        model = File
        fields = ('name', 'file',)