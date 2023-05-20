from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
def drink_list(request):
    # get all the drinks
    drinks= Drink.objects.all()
    # instance of the DrinkSerializer class
    serializer= DrinkSerializer(drinks, many=True)
    return JsonResponse({"drinks":serializer.data}, safe=False)

