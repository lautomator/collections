from django import forms


# uploader class
class UploadFileForm(forms.Form):
    file = forms.FileField()
