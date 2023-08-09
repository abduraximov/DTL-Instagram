from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from apps.common.models import BaseModel


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(_('Full name'), max_length=64)
    avatar = models.ImageField(upload_to='profile/avatars/', default='default_avatar.png', blank=True)
    last_active_time = models.DateTimeField(_('Last active time'), blank=True)
    online = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.full_name
    

class Following(BaseModel):
    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='followings',
        verbose_name=_("User")
    )
    followed_user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='followers',
        verbose_name=_("Followed user")
    )

    def __str__(self):
        return f"{self.user.username} to {self.followed_user.username}"


class Message(BaseModel):
    text = models.TextField(_("Message body"))
    sender = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        related_name='sending_messages',
        verbose_name=_("Sender"),
        null=True
    )
    receiver = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        related_name='received_messages',
        verbose_name=_("Receiver"),
        null=True
    )
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.text