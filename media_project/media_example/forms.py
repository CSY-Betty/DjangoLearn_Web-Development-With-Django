from django import forms
from .models import ExampleModel


class UploadForm(forms.Form):
    class Meta:
        model = ExampleModel
        fields = "__all__"
