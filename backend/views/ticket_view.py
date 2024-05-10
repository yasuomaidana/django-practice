from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from backend.models import Ticket
from serializer.ticket_serializer import TicketSerializer, TicketCreateSerializer


class TicketViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Ticket.objects.all()
    lookup_field = 'category'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TicketSerializer
        elif self.request.method == 'POST':
            return TicketCreateSerializer
        return TicketSerializer  # you can also customize for update/delete if needed

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)