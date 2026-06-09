from django import forms
from lawyerapp.models import Lawyer,Services
from clientapp.models import Add_Queries

class LawyerForm(forms.ModelForm):
    class Meta:
        model = Lawyer
        exclude = ["status"]

class ServicesForms(forms.ModelForm):
    class Meta:
        model = Services

        fields = "__all__"

class Queries_RepliesForms(forms.ModelForm):
    class Meta:
        model = Add_Queries

        fields = ["reply_queries"]


