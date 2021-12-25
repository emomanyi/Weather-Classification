from django import forms
from .models import UploadModel
class WeatherForm(forms.ModelForm):
    
    class Meta:
        model = UploadModel
        fields = ['file']
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['file'].widget.attrs.update({'class':'form-control'})