from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.models import UserOrder
from users.serializers import UserOrderSerializer


@api_view(['GET', 'DELETE', 'POST', 'PUT'])
def order_meal(request, pk):
    if request.method == 'GET':
        if not request.user.username:
            return Response({})
        return Response([UserOrderSerializer(order).data for order in
                         list(UserOrder.objects.filter(user=request.user))])
        # return Response({})
    elif request.method == 'DELETE':
        return Response({})
    elif request.method == 'POST':
        return Response({})
    elif request.method == 'PUT':
        return Response({})
