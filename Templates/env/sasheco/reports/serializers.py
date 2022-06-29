from dataclasses import fields
from rest_framework import serializers
from reports.models import Guest, Moive, Reservation


class Movieserializer(serializers.ModelSerializer):
    class Meta:
        model = Moive
        fields = '__all__'


class Reservationserializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'


class Guestserializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['pk', 'reservation', 'name', 'mobile']
