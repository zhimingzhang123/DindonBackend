from rest_framework.generics import ListAPIView

from Announcements.models import Announcement
from Announcements.serializers import AnnouncementSerializer


class AnnouncementListView(ListAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
