from django.urls import path

from . import views

urlpatterns = [
    path('<slug:short_slug>', views.shortened_url_redirect)
]
