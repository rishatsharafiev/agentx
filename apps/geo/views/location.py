from django.utils import timezone
from utils.decorators import json_request, json_response
from utils.views import BaseView

from ..forms import LocationForm
from ..models import Location


class LocationView(BaseView):
    """Location View"""

    @json_response
    def get(self, request, pk=None):
        """Get location"""
        locations = Location.objects.filter(employee__pk=pk).order_by('-created_at')

        response = {
            "apiVersion": "1.0",
            "id": pk,
            "method": "GET",
            "data": {
                "kind": "employee",
                "fields": "latitude,longitude,created_at",
                "items": [{"latitude": location.latitude,
                           "longitude": location.longitude,
                           "created_at": timezone.localtime(location.created_at),
                           } for location in locations]
            }
        }

        return response

    @json_response
    @json_request
    def post(self, request):
        """Post location"""
        json = request.json

        if json:
            location_form = LocationForm(json)
            if location_form.is_valid():
                response = {
                    "data": {
                        "kind": "employee",
                        "fields": "id,first_name,last_name",
                    }
                }
            else:
                response = {
                    'error': {
                        'code': 422,
                        'message': 'Validation Error',
                        'errors': location_form.errors
                    }
                }
        else:
            response = {
                'error': {
                    'code': 404,
                    'message': 'Empty json',
                }
            }

        return response
