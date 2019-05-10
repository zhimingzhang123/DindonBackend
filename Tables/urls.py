from django.urls import path

from Tables.views import TableListView, TableUpdateView

urlpatterns = [
    path('', TableListView.as_view()),
    path('<int:pk>/', TableUpdateView.as_view()),
]
