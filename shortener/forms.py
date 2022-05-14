from django import forms

from .models import Link


class AddLinkForm(forms.ModelForm):
    full_link = forms.URLField(widget=forms.URLInput(
        attrs={"class": "form-control form-control-lg", "placeholder": "Ваша ссылка для сокращения..."}
    ))

    class Meta:
        model = Link
        fields = 'full_link',
