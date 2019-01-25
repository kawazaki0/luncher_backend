from rest_framework import viewsets
from .models import Restaurant, MealCategory
from .serializers import RestaurantSerializer, RestaurantDetailSerializer, MealCategorySerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()

    def get_serializer_class(self):
        if self.get_view_name() == 'Restaurant Instance':
            return RestaurantDetailSerializer
        else:
            return RestaurantSerializer


class MealCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = MealCategorySerializer
    queryset = MealCategory.objects.all()

