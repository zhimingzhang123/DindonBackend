from django.urls import path

from Tables.views import TableListView

urlpatterns = [
    path('', TableListView.as_view()),
]
