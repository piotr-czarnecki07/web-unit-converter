from django.db import models

class Base(models.Model):
    class Meta:
        abstract = True

    input_value = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): # @abstractmethod was resulting in an error
        try:
            return f"input_value: {self.input_value}, input_unit: {self.input_unit}, output_unit: {self.output_unit}"
        except:
            return "Object's __str__ method called on an abstract class" # probably won't ever happen

class ConvertLength(Base):
    OPTIONS = [
        ('-', '-'),
        ('millimeter', 'Millimeter'),
        ('centimeter', 'Centimeter'),
        ('meter', 'Meter'),
        ('kilometer', 'Kilometer'),
        ('inch', 'Inch'),
        ('foot', 'Foot'),
        ('yard', 'Yard'),
        ('mile', 'Mile')
    ]

    input_unit = models.CharField(max_length=50, choices=OPTIONS, default='-')
    output_unit = models.CharField(max_length=50, choices=OPTIONS, default='-')

class ConvertMass(Base):
    OPTIONS = [
        ('-', '-'),
        ('milligram', 'Milligram'),
        ('gram', 'Gram'),
        ('kilogram', 'Kilogram'),
        ('ounce', 'Ounce'),
        ('pound', 'Pound')
    ]

    input_unit = models.CharField(max_length=50, choices=OPTIONS, default='-')
    output_unit = models.CharField(max_length=50, choices=OPTIONS, default='-')

class ConvertTemperature(Base):
    OPTIONS = [
        ('-', '-'),
        ('celsius', 'Celsius'),
        ('fahrenheit', 'Fahrenheit'),
        ('kelvin', 'Kelvin')
    ]

    input_unit = models.CharField(max_length=50, choices=OPTIONS, default='-')
    output_unit = models.CharField(max_length=50, choices=OPTIONS, default='-')