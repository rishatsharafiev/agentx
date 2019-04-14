from django.forms import ModelForm

from ..models import Location


class LocationForm(ModelForm):
    """Location Form"""

    class Meta:
        """Meta Class"""

        model = Location
        fields = ['latitude', 'longitude']
