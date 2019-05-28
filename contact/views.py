from django.views.generic import TemplateView
from contact.models import Person


class ContactView(TemplateView):
    template_name = 'contact/view.html'

    def get_context_data(self, **kwargs):
        return {
            'contacts': Person.objects.filter(is_friend=True)
        }

