from rest_framework import serializers

from carsapp.models import Car, Moto


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = '__all__'
        # fields = ('title', 'description',)


class MotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Moto
        fields = '__all__'
        # fields = ('title', 'description',)