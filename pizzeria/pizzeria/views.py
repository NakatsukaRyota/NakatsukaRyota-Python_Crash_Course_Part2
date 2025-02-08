from django.shortcuts import render

from .models import Pizza


def index(request):
    return render(request, "pizzeria/index.html")


def pizzas(request):
    pizzas = Pizza.objects.order_by("date_added")
    context = {"pizzas": pizzas}
    return render(request, "pizzeria/pizzas.html", context)


def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by("-date_added")
    context = {"pizza": pizza, "toppings": toppings}
    return render(request, "pizzeria/pizza.html", context)
