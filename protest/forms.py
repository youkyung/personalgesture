from django import forms
from protest.models import Protest

class ProtestForm(forms.ModelForm):
    class Meta :
        model = Protest
        fields = '__all__'