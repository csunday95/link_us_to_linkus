from django.http import HttpRequest
from django.shortcuts import redirect, get_object_or_404
from .models import *


# Create your views here.
def shortened_url_redirect(request: HttpRequest, short_slug: str):
    shorten_model_instance = get_object_or_404(ShortenedURLModel, shortened_url_slug=short_slug)
    full_url = shorten_model_instance.full_url
    return redirect(full_url)
