from django.contrib import admin
from django.urls import path

from contact.api import ContactAPI
from contact.views import ContactView, ContactAddView, ContactAddFailView, ContactAddFormView, ContactAddSuccessView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', ContactView.as_view()),
    path('contact/', ContactAPI.as_view()),
    path('contact/add/success/', ContactAddSuccessView.as_view(), name='contact-add-success'),
    path('contact/add/fail/', ContactAddFailView.as_view(), name='contact-add-fail'),
    path('contact/add/db/', ContactAddView.as_view(), name='contact-add-db'),
    path('contact/add/', ContactAddFormView.as_view(), name='contact-add-form'),
]
