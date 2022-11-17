from django import forms
from django.core import validators
from deepl.translator_engine import available_languages 

languages_list=[(value, key) for key, value in available_languages.items()]

class TranslateForm(forms.Form):
    source_language = forms.ChoiceField(choices=languages_list, widget=forms.Select(
        attrs={'class': 'form-control language-sel'}))
    source_text = forms.CharField(max_length=200, widget=forms.Textarea(
        attrs={'class': 'form-control text-area', 'cols': '40', 'rows': '8'}))
    target_language = forms.ChoiceField(choices=languages_list, widget=forms.Select(
        attrs={'class': 'form-control language-sel'}))
    target_text = forms.CharField(max_length=200, widget=forms.Textarea(
        attrs={'class': 'form-control text-area', 'cols': '40', 'rows': '8'}), required=False)
