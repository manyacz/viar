from rest_framework import serializers
from .models import Rooms

class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = ('title', 'content', 'photo', 'price', 'is_published', 'date_start', 'date_end')