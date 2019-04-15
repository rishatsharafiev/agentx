from utils.decorators import json_response
from utils.shortcuts import daterange, move_point
from utils.views import BaseView

from ..forms import LocationParametersForm
from ..models import Employee, Location


class LocationGenerateView(BaseView):
    """Location Generate View"""

    @json_response
    def get(self, request, pk=None):
        """Generate location"""
        try:
            employee = Employee.objects.get(pk=pk)

            created_at__gte = request.GET.get('created_at__gte', None)
            created_at__lt = request.GET.get('created_at__lt', None)
            latitude = request.GET.get('latitude', None)
            longitude = request.GET.get('longitude', None)

            location_parameters_form = LocationParametersForm({
                'created_at__gte': created_at__gte,
                'created_at__lt': created_at__lt,
                'latitude': latitude,
                'longitude': longitude,
            })

            if location_parameters_form.is_valid():
                items = []
                daterange_generator = daterange(
                    location_parameters_form.cleaned_data['created_at__gte'],
                    location_parameters_form.cleaned_data['created_at__lt'],
                )
                latitude = location_parameters_form.cleaned_data['latitude']
                longitude = location_parameters_form.cleaned_data['longitude']

                for created_at in daterange_generator:
                    location = Location(employee=employee, latitude=latitude, longitude=longitude)
                    location.created_at = created_at
                    location.save()
                    items.append({
                        'latitude': location.latitude,
                        'longitude': location.longitude,
                        'created_at': location.created_at
                    })
                    latitude, longitude = move_point(latitude, longitude)

                response = {
                    'data': {
                        'items': items
                    }
                }
            else:
                response = {
                    'error': {
                        'code': 422,
                        'message': 'Validation Error',
                        'errors': location_parameters_form.errors
                    }
                }
        except Employee.DoesNotExist as exp:
            response = {
                'error': {
                    'code': 404,
                    'message': str(exp),
                }
            }

        return response
