from django import forms


class LocationParametersForm(forms.Form):
    """Location Parameters Form"""

    latitude = forms.DecimalField(label='Широта', max_digits=9, decimal_places=6, required=True)
    longitude = forms.DecimalField(label='Долгота', max_digits=9, decimal_places=6, required=True)
    created_at__gte = forms.DateTimeField(label='Начало', required=True)
    created_at__lt = forms.DateTimeField(label='Конец', required=True)
