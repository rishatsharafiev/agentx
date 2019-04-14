from utils.decorators import json_request, json_response
from utils.views import BaseView


class EmployeeView(BaseView):
    """Employee View"""

    @json_response
    def get(self, request):
        """Get employee"""
        response_error = {
            'error': {
                'code': 405,
                'message': "File Not Found",
                'errors': [],
            }
        }

        return response_error

    @json_response
    @json_request
    def post(self, request):
        """Post employee"""
        response_data = {
            "apiVersion": "1.0",
            "id": 123,
            "method": "POST",
            "data": {
                "kind": "album",
                "fields": "author,id",
                "id": 12,
                "json": request.json
            }
        }

        return response_data
