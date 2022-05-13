from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect, reverse


class Logout(LogoutView):
    def get(self, request, *args, **kwargs):
        return redirect(reverse('home'))
