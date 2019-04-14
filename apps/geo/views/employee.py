from utils.decorators import json_response
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

        # response_data = {
        #     "apiVersion": "1.0",
        #     "id": 123,
        #     "method": "POST",
        #     "data": {
        #         "kind": "album",
        #         "fields": "author,id",
        #         "id": 12,
        #         "updated": "2007-11-06T16:34:41.000Z",
        #         "items": [
        #             {
        #                 "title": "A deleted entry",
        #                 "deleted": True
        #             }
        #         ]
        #     }
        # }

        return response_error
