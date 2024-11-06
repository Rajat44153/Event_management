from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import User, Event, Ticket
from .serializers import UserSerializer, EventSerializer, TicketSerializer
from django.db.models import F

# Register User (Both Admin and User can register)
class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Admin-only Event Management (Create Event)
class EventCreateView(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAdminUser]

# List Events (Accessible to Admin and User)
class EventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

# Purchase Tickets (User-only)
class TicketPurchaseView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def create(self, request, *args, **kwargs):
        event = Event.objects.get(id=kwargs['event_id'])
        quantity = request.data.get('quantity')

        if event.tickets_sold + quantity > event.total_tickets:
            return Response({"error": "Not enough tickets available"}, status=status.HTTP_400_BAD_REQUEST)

        # Create ticket
        ticket = Ticket.objects.create(user=request.user, event=event, quantity=quantity)
        event.tickets_sold += quantity
        event.save()

        return Response(TicketSerializer(ticket).data, status=status.HTTP_201_CREATED)

