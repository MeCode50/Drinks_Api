from rest_framework import serializers
from .models import Drink
class DrinkSerializer(serializers.ModelSerializer):
    # inner class meta data describing the mosel
    class Meta:
        model = Drink
        fields = ["id","name","description"]
        