from django.contrib import admin
from django.urls import path
from contact.views import ContactView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', ContactView.as_view())
]
