from django.urls import path, include
from app_ticket.views import homepage, person_create_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('homepage/', homepage, name="homepage"),
      path('response/', person_create_view, name="response"),
]

