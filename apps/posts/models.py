from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _
from apps.common.models import BaseModel
from apps.profiles.models import Profile


class Post(BaseModel):
    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name=_('User')
    )
    caption = models.TextField(_('Caption'))
    like_count = models.PositiveIntegerField(_('Likes'), default=0)
    media = models.FileField(
        upload_to='post/media/',
        validators=[
            FileExtensionValidator(
                allowed_extensions=['mp4', 'gif', 'jpg', 'png']
            )
        ],
        verbose_name=_('Images or videos')
    )

    def __str__(self):
        return self.caption


class Saved(BaseModel):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name=_('Post')
    )
    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='saved_posts',
        verbose_name=_('User')
    )


class Liked(BaseModel):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='likes',
        verbose_name=_('Post')
    )
    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='liked_posts',
        verbose_name=_('User')
    )


class Comment(BaseModel):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name=_('Post')
    )
    user = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        related_name='comments',
        verbose_name=_('User'),
        null=True
    )
    text = models.TextField(_('Text'))

    def __str__(self) -> str:
        return self.text
