from django.db import models
from django.conf import settings

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class Message(models.Model):
    """
    A private message from user to user, on delete removes recipient name with null.
    """
    title = models.CharField("Title", max_length=200)
    body = models.TextField("Body")
    sender = models.ForeignKey(AUTH_USER_MODEL, related_name='sent_messages',
                               verbose_name="Sender", on_delete=models.PROTECT)
    recipient = models.ForeignKey(
        AUTH_USER_MODEL, null=True, blank=True, verbose_name="Recipient", on_delete=models.SET_NULL)
    sent_at = models.DateTimeField("Sent at", auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-sent_at']
