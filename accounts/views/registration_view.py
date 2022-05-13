from django.urls import reverse_lazy
from django.views.generic import CreateView


from ..forms import UserRegistrationForm


class RegisterUser(CreateView):
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


