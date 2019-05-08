from django.urls import path

from Announcements.views import AnnouncementListView

urlpatterns = [
    path('', AnnouncementListView.as_view()),
]
