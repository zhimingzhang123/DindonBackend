from django.urls import path

from Dishes.views import DishListView

urlpatterns = [
    path('', DishListView.as_view()),
]
