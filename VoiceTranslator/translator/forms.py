from django import forms

available_languages = (
    ("PL", "Polski"),
    ("EN", "English")
)


class TranslateForm(forms.Form):
    input_language = forms.ChoiceField(choices=available_languages, widget=forms.Select(
        attrs={'class': 'form-control language-sel'}))
    input_text = forms.CharField(max_length=200, widget=forms.Textarea(
        attrs={'class': 'form-control text-area', 'cols': '40', 'rows': '8'}))
    target_language = forms.ChoiceField(choices=available_languages, widget=forms.Select(
        attrs={'class': 'form-control language-sel'}))
    target_text = forms.CharField(max_length=200, widget=forms.Textarea(
        attrs={'class': 'form-control text-area', 'cols': '40', 'rows': '8'}))
