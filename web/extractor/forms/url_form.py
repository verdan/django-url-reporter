from django.core.validators import URLValidator
from django.forms import forms, URLInput


class UrlForm(forms.Form):
    url = forms.Field(widget=URLInput(), required=True, label='Paste your URL here')

    def clean_url(self):
        url = self.cleaned_data.get('url')
        try:
            validator = URLValidator()
            validator(url)
        except forms.ValidationError:
            raise forms.ValidationError('Please enter a valid URL.')
        return url