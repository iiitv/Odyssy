from rest_framework.serializers import ModelSerializer
from taggit_serializer.serializers import (
    TagListSerializerField,
    TaggitSerializer
)

from ..models import Announcement


class AnnouncementSerializer(TaggitSerializer, ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Announcement
        fields = [
            'key',
            'start_date',
            'end_date',
            'title',
            'description',
            'tags',
        ]
