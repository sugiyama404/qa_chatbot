from rest_framework import serializers

from .models import Ghostintheshell

class GhostintheshellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ghostintheshell
        fields = '__all__'
