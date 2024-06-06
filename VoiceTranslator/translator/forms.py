from django import forms
from .models import Language
from django.db.utils import OperationalError

try:
    languages_list=[(i.translate_short, i.language) for i in Language.objects.all()]
except OperationalError:
    pass

class TranslateForm(forms.Form):
    source_language = forms.ChoiceField(choices=languages_list, widget=forms.Select(
        attrs={'class': 'form-control language-sel'}), initial=("EN"))
    source_text = forms.CharField(max_length=200, required=False, widget=forms.Textarea(
        attrs={'class': 'form-control text-area'}))
    target_language = forms.ChoiceField(choices=languages_list, widget=forms.Select(
        attrs={'class': 'form-control language-sel'}), initial=("PL"))
    target_text = forms.CharField(max_length=200, widget=forms.Textarea(
        attrs={'class': 'form-control text-area'}), required=False)
    
