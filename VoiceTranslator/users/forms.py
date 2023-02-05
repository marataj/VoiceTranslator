from django import forms


class LoginForm(forms.Form):
    """
    Login form, with the specific fields declared.

    """

    username = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
