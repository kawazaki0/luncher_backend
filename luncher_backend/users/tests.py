from django.test import TestCase, Client
from rest_framework import status
from rest_framework.reverse import reverse

from restaurants.models import Meal, Restaurant
from users.models import UserOrder, User

client = Client()


class GetOrdersTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.user.set_password('pass')
        self.user.save()
        restaurant = Restaurant(email='xaxa', name='rest')
        restaurant.save()
        self.meal = Meal.objects.create(name='meal', restaurant=restaurant,
                                        price=12)
        UserOrder(user=self.user, meal=self.meal).save()

    def test_get_orders(self):
        client.login(username='testuser', password='pass')
        response = client.get(reverse('orders'))
        # orders = UserOrder.objects.filter(user=self.user)

        self.assertEqual(response.data,
                         [{'user': self.user.id, 'meal': self.meal.id}])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
