from django.forms import ModelForm
from .models import Palavra


class PalavraNovaForm(ModelForm):
    class Meta:
        model = Palavra
        fields = ['nome']
