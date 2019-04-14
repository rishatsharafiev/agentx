from django.core.exceptions import ValidationError
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
        try:
            created_at__gte = request.GET.get('created_at__gte', '1900-01-01')
            created_at__lte = request.GET.get('created_at__lte', '3000-01-01')

            locations = Location.objects.filter(created_at__gte=created_at__gte,
                                                created_at__lte=created_at__lte,
                                                employee__pk=pk).order_by('-created_at')
            items = [{
                "latitude": location.latitude,
                "longitude": location.longitude,
                "created_at": timezone.localtime(location.created_at)
            } for location in locations]
            
            response = {
                "apiVersion": "1.0",
                "id": pk,
                "method": "GET",
                "data": {
                    "kind": "employee",
                    "fields": "latitude,longitude,created_at",
                    "items": items
                }
            }
        except ValidationError as exp:
            response = {
                'error': {
                    'code': 422,
                    'message': 'Validation Error',
                    'errors': str(exp)
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
