from rest_framework import serializers

from xai_backend.models import Song, TopSong


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopSong
        fields = '__all__'

