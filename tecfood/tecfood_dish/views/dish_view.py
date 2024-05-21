from rest_framework import viewsets
from tecfood_dish.models import Dish
from tecfood_dish.serializers import DishSerializer

class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer