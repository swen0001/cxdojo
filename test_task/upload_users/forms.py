from django import forms
from .models import Files


class FilesModelForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ('file_csv', "file_xml",)
        widget = forms.FileInput()
