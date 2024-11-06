from django.urls import path
from .views import UserRegisterView, EventCreateView, EventListView, TicketPurchaseView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user_register'),
    path('events/', EventListView.as_view(), name='event_list'),
    path('events/create/', EventCreateView.as_view(), name='event_create'),
    path('events/<int:event_id>/purchase/', TicketPurchaseView.as_view(), name='ticket_purchase'),
]
