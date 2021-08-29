from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField, SlugRelatedField, CurrentUserDefault, PrimaryKeyRelatedField
from messaging.models import Message
from rest_framework.fields import CurrentUserDefault


class UserSerializer(ModelSerializer):
    """Serializing using dj User model to exclude other fields from default"""
    password = CharField(write_only=True)
    # write_only=True avoids getting the password displayed on GET request, only POST for creation of user

    class Meta:
        model = User
        fields = ['username', 'password']


class MessageSerializer(ModelSerializer):
    recipient = CharField(read_only=True, default=CurrentUserDefault())
    sender = CharField(read_only=True, default=CurrentUserDefault())
    # recipient and sender formatted to display string of name rather than primary key

    class Meta:
        model = Message
        fields = '__all__'
