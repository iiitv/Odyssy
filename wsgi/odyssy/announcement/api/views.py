from rest_framework.generics import ListAPIView

from .serializer import AnnouncementSerializer
from ..models import Announcement


class AnnouncementListView(ListAPIView):
    """ All announcement list view """
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer


class AnnouncementParticularView(ListAPIView):
    """ Particular announcement view from key """
    serializer_class = AnnouncementSerializer

    def get_queryset(self):
        """
        Filter a particular annouuncement based
        upon the key value
        """
        return Announcement.get_single_announcement(self.kwargs['key'])

class AnnouncementTagView(ListAPIView):
    """ Returns announcement based upon tags """
    serializer_class = AnnouncementSerializer

    def get_queryset(self):
        """
        Filters announcement based upon tag
        system
        """
        return Announcement.get_announcement_tag(self.kwargs['tag_name'])


class AnnouncementLatestView(ListAPIView):
    """ Returns the latest announcements """
    serializer_class = AnnouncementSerializer

    def get_queryset(self):
        """
        Returns the number of latest announcements
        """
        return Announcement.get_latest_announcements(self.kwargs['cnt'])
