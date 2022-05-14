from django.urls import path

from .views import HomeView, shortener_view, redirect_url_view

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('shortener/', shortener_view, name='shortener'),
    path('<str:shortened_part>', redirect_url_view, name='redirect'),
]
