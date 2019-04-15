from django.utils import timezone
from utils.decorators import json_response
from utils.views import BaseView

from ..models import Location


class EmployeeLocationView(BaseView):
    """Employee Location View"""

    @json_response
    def get(self, request):
        """Get location"""
        locations = Location.objects.prefetch_related('employee') \
            .order_by('employee_id', '-created_at').distinct('employee_id')

        items = [{
            "id": location.employee.id,
            "first_name": location.employee.first_name,
            "last_name": location.employee.last_name,
            "latitude": location.latitude,
            "longitude": location.longitude,
            "created_at": timezone.localtime(location.created_at)
        } for location in locations]

        response = {
            "apiVersion": "1.0",
            "method": "GET",
            "data": {
                "kind": "employee",
                "fields": "id,first_name,last_name,latitude,longitude,created_at",
                "items": items
            }
        }

        return response
