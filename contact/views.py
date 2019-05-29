from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, View

from contact.forms import PersonForm
from contact.models import Person


class ContactView(TemplateView):
    template_name = 'contact/view.html'

    def get_context_data(self, **kwargs):
        return {
            'contacts': Person.objects.all()
        }


class ContactAddFormView(TemplateView):
    template_name = 'contact/form.html'

    def get_context_data(self, **kwargs):
        form = PersonForm()
        return locals()


class ContactAddSuccessView(TemplateView):
    template_name = 'contact/success.html'


class ContactAddFailView(TemplateView):
    template_name = 'contact/fail.html'


class ContactAddView(View):
    def get(self, request):
        return HttpResponseRedirect(reverse('contact-add-fail'))

    def post(self, request):
        form = PersonForm(request.POST)

        if not form.is_valid():
            return HttpResponseRedirect(reverse('register-fail'))

        Person.objects.create(
            first_name=form.cleaned_data.get('first_name'),
            last_name=form.cleaned_data.get('last_name'),
            date_of_birth=form.cleaned_data.get('date_of_birth'),
            add_author=request.user,
            modified_author=request.user,
        )

        return HttpResponseRedirect(reverse('contact-add-success'))
