from dataclasses import fields
from rest_framwork import serializers
from reports.models import Guest, Moive, Reservation


class Movieserializer(serializers.ModelSerializer):
    class Meta:
        Model = Moive
        fields = '__all__'


class Reservationserializer(serializers.ModelSerializer):
    class meta:
        model = Reservation
        fields = '__all__'


class Guestserializer(serializers.ModelSerializer):
    class meta:
        model = Guest
        fields = ['pk', 'Reservation', 'name', 'mobile']
