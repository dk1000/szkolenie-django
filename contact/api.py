from http import HTTPStatus
from django.http import JsonResponse
from django.views.generic import View
from contact.models import Person


class ContactAPI(View):
    def get(self, request):
        qs = Person.objects.all().values()
        return JsonResponse(status=HTTPStatus.OK, data=list(qs), safe=False)
