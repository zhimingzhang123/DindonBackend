from rest_framework.response import Response
from rest_framework.views import APIView

from Announcements.models import Announcement
from Announcements.serializers import AnnouncementSerializer


class AnnouncementListView(APIView):
    def get(self, request):
        announcements = Announcement.objects.all()
        serializer = AnnouncementSerializer(announcements, many=True)
        return Response(serializer.data)
