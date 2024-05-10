from rest_framework import serializers

from backend.models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'  # To include all fields from the Ticket model


class TicketCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('category', 'description')  # Explicitly mentioning fields for creation


