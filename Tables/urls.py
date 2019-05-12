from django.urls import path

from Tables.views import TableListView, BookTableView

urlpatterns = [
    path('', TableListView.as_view()),
    path('books', BookTableView.as_view()),
]
