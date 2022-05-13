from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)


class ResetPassword(PasswordResetView):
    template_name = 'accounts/reset_password.html'


class ResetPasswordDone(PasswordResetDoneView):
    template_name = 'accounts/reset_password_done.html'


class ConfirmResetPassword(PasswordResetConfirmView):
    template_name = 'accounts/confirm_reset_password.html'


class CompleteResetPassword(PasswordResetCompleteView):
    template_name = 'accounts/complete_reset_password.html'