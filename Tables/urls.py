from django.urls import path

from Tables.views import TableListView, TableView

urlpatterns = [
    path('', TableListView.as_view()),
    path('<int:pk>/', TableView.as_view()),
]
