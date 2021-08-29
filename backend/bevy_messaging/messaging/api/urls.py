from django.urls import path
from.views import ComposeAPIView, RecievedListAPIView, SentListAPIView, ReadMessageAPIView

urlpatterns = [
    path('recieved_messages', RecievedListAPIView.as_view(),
         name='recieved_messages_list'),
    path('sent_messages', SentListAPIView.as_view(), name='sent_messages_list'),
    path('compose_message', ComposeAPIView.as_view(),
         name='compose_message_create'),
    path('read_message/<int:pk>/', ReadMessageAPIView.as_view(),
         name='retrieve_detail_delete'),
]
