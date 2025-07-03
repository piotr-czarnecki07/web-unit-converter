from django.forms import ModelForm
from .models import ConvertLength, ConvertMass, ConvertTemperature

class ConvertLengthForm(ModelForm):
    class Meta:
        model = ConvertLength
        fields = ['input_value', 'input_unit', 'output_unit']

class ConvertMassForm(ModelForm):
    class Meta:
        model = ConvertMass
        fields = ['input_value', 'input_unit', 'output_unit']

class ConvertTemperatureForm(ModelForm):
    class Meta:
        model = ConvertTemperature
        fields = ['input_value', 'input_unit', 'output_unit']