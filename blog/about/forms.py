from django import forms
from django.forms import fields
from about.models import WishMessage

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    message = forms.CharField(max_length=500, widget=forms.Textarea)
    email = forms.EmailField()
    allow_mailing = forms.BooleanField()

class ContactModelForm(forms.ModelForm):
    class Meta:
        model = WishMessage
        fields = "__all__"