from django import forms
from blog.models import Protest

class ProtestForm(forms.ModelForm):
    class Meta :
        model = Protest
        fields = '__all__'