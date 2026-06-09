from django import forms
from lawapp.models import Contact, Notifications


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class NotificationsForm(forms.ModelForm):
    class Meta:
        model = Notifications
        exclude = ["date_time"]
