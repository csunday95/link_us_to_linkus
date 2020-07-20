from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
import random
import string


ENTRY_NAME_MAX_LENGTH = 128
FULL_URL_MAX_LENGTH = 512
SHORTENED_URL_MAX_LENGTH = 64


class ShortenedURLModel(models.Model):
    class Meta:
        verbose_name = 'Shortened URL Model'
        verbose_name_plural = 'Shortened URL Models'

    entry_name = models.CharField(
        max_length=ENTRY_NAME_MAX_LENGTH,
        verbose_name='Entry Name',
        help_text='A human readable name for this shortened URL'
    )
    full_url = models.URLField(
        max_length=FULL_URL_MAX_LENGTH,
        unique=True,
        verbose_name='Full URL',
        help_text='The full URL that will be redirected to'
    )
    shortened_url_slug = models.SlugField(
        max_length=SHORTENED_URL_MAX_LENGTH,
        unique=True,
        verbose_name='Shortened URL',
        help_text='The shortened version of the URL'
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        url_edges = '{}...{}'.format(self.full_url[:16], self.full_url[-6:])
        return f'{self.entry_name} <{self.shortened_url_slug} -> {url_edges}>'

