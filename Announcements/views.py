from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from Announcements.models import Announcement
from Announcements.serializers import AnnouncementSerializer


class AnnouncementListView(ListAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
