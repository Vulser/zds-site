# coding: utf-8

from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms_foundation.layout import Field, Layout, Div, HTML

from zds.newsletter.models import Newsletter


class NewsletterForm(forms.Form):

    email = forms.EmailField(
        label='',
        max_length=Newsletter._meta.get_field('email').max_length,
        required=True,
    )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            Field('email', placeholder="E-mail"),
            Div(
                HTML('<button type="submit" title="Inscription newsletter"><span>OK</span></button>'),
            ))
        super(NewsletterForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(NewsletterForm, self).clean()

        email = cleaned_data.get('email')

        # Check that the email is unique
        if Newsletter.objects.filter(email=email).count() > 0:
            msg = u'Votre adresse email est déjà utilisée'
            self._errors['email'] = self.error_class([msg])
            if 'email' in cleaned_data:
                del cleaned_data['email']

        return cleaned_data