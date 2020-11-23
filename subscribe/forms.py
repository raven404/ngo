from django import forms
from .models import Signup


class EmailSignupForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        "type": "email",
        "name": "email",
        "id": "email",
        "placeholder": "Enter your email address",
        "class": "form-control fh5co_footer_text_box",
        "aria-describedby": "basic-addon1",

    }), label="")

    class Meta:
        model = Signup
        fields = ('email', )
