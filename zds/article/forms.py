# coding: utf-8

from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms_foundation.layout import Layout, Submit, Field
from zds.utils.models import SubCategory


class ArticleForm(forms.Form):
    title = forms.CharField(
        label='Titre',
        max_length=80
    )

    description = forms.CharField(
        max_length=200
    )
    
    text = forms.CharField(
        label='Texte',
        required=False,
        widget=forms.Textarea
    )
    
    image = forms.ImageField(
        label='Selectionnez une image', 
        required=False)

    subcategory = forms.ModelMultipleChoiceField(
        label = "Sous catégories de votre article",
        queryset = SubCategory.objects.all(),
        required = False
    )

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.layout1 = Layout(
            Field('title'),
            Field('description'),
        )
        self.helper.layout2 = Layout(
            Field('text'),
            Field('image'),
            Field('subcategory'),
            Submit('submit', 'Valider'),
        )

class ReactionForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)


class AlertForm(forms.Form):
    text = forms.CharField()