from django.urls import path

from .views import (
    Login,
    Logout,
    ResetPassword,
    ResetPasswordDone,
    ConfirmResetPassword,
    CompleteResetPassword,
    RegisterUser,
)


urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('reset-password/', ResetPassword.as_view(), name='reset_password'),
    path('password-reset/done/', ResetPasswordDone.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', ConfirmResetPassword.as_view(), name='password_reset_confirm'),
    path('reset/done/', CompleteResetPassword.as_view(), name='password_reset_complete'),
    path('register/', RegisterUser.as_view(), name='register'),
]
