from django.urls import path

from Dishes.views import DishListView, DishTypeView

urlpatterns = [
    path('lists/', DishListView.as_view()),
    path('types/', DishTypeView.as_view())
]
