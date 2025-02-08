"""pizzeriaのURLパターンの定義"""

from django.urls import path

from . import views

app_name = "pizzeria"
urlpatterns = [
    # ホームページ
    path("", views.index, name="index"),
    path("pizzas/", views.pizzas, name="pizzas"),
    path("pizzas/<int:pizza_id>/", views.pizza, name="pizza"),
]
