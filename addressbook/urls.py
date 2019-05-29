from django.contrib import admin
from django.urls import path, include
from django.conf import settings
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

if settings.DEBUG and settings.DEBUG_TOOLBAR:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
