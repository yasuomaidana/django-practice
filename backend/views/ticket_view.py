from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from backend.models import Ticket
from serializer.ticket_serializer import TicketSerializer, TicketCreateSerializer, DescriptionSerializer


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


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = DescriptionSerializer
    queryset = Ticket.objects.all()

    def get_queryset(self):
        ticket_id = list(self.kwargs.values())[0]
        return Ticket.objects.get(id=ticket_id)

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=False)
            return Response(serializer.data)
        except Ticket.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
