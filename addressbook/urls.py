from django.contrib import admin
from django.urls import path

from contact.api import ContactAPI
from contact.views import ContactView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', ContactView.as_view()),
    path('contact/', ContactAPI.as_view())
]
