from django.forms import ModelForm
from .models import Service

class ServiceFrom(ModelForm):
    class Meta:
        model=Service
        fields=['typeofservice','nameofservice','startdate','description']
