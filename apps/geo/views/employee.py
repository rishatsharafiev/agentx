from utils.decorators import json_request, json_response
from utils.views import BaseView

from ..forms import EmployeeForm
from ..models import Employee


class EmployeeView(BaseView):
    """Employee View"""

    @json_response
    def get(self, request, pk=None):
        """Get employee"""
        try:
            employee = Employee.objects.get(pk=pk)
            response = {
                "apiVersion": "1.0",
                "id": employee.id,
                "method": "GET",
                "data": {
                    "kind": "employee",
                    "fields": "id,first_name,last_name",
                    "id": employee.id,
                    "first_name": employee.first_name,
                    "last_name": employee.last_name,
                    "gender": employee.get_gender_name(),
                    "birth_day": employee.birth_day,
                    "email": employee.email,
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

    @json_response
    @json_request
    def post(self, request):
        """Post employee"""
        json = request.json

        if json:
            employee_form = EmployeeForm(json)
            if employee_form.is_valid():
                employee = employee_form.save()

                response = {
                    "data": {
                        "kind": "employee",
                        "fields": "id,first_name,last_name",
                        "id": employee.id,
                        "first_name": employee.first_name,
                        "last_name": employee.last_name,
                        "gender": employee.get_gender_name(),
                        "birth_day": employee.birth_day,
                        "email": employee.email,
                    }
                }
            else:
                response = {
                    'error': {
                        'code': 422,
                        'message': 'Validation Error',
                        'errors': employee_form.errors
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

    @json_response
    @json_request
    def patch(self, request, pk=None):
        """Patch employee"""
        try:
            employee = Employee.objects.get(pk=pk)
            json = request.json

            if json:
                employee_form = EmployeeForm(json, instance=employee)
                employee_form.fields['first_name'].required = False
                employee_form.fields['last_name'].required = False

                if employee_form.is_valid():
                    employee.save(update_fields=json.keys())

                    response = {
                        "data": {
                            "kind": "employee",
                            "id": employee.id
                        }
                    }

                    fields = ["id"]
                    if employee.first_name is not None:
                        response["data"]["first_name"] = employee.first_name
                        fields.append("first_name")
                    if employee.last_name is not None:
                        response["data"]["last_name"] = employee.last_name
                        fields.append("last_name")
                    if employee.gender is not None:
                        response["data"]["gender"] = employee.get_gender_name()
                        fields.append("gender")
                    if employee.birth_day is not None:
                        response["data"]["birth_day"] = employee.birth_day
                        fields.append("birth_day")
                    if employee.email is not None:
                        response["data"]["email"] = employee.email
                        fields.append("email")
                    response["data"]["fields"] = ",".join(fields)
                else:
                    response = {
                        'error': {
                            'code': 422,
                            'message': 'Validation Error',
                            'errors': employee_form.errors
                        }
                    }
            else:
                response = {
                    'error': {
                        'code': 404,
                        'message': 'Empty json',
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

    @json_response
    def delete(self, request, pk=None):
        """Delete employee"""
        employee_id, _ = Employee.objects.filter(pk=pk).delete()

        if employee_id:
            response = {
                "data": {
                    "kind": "employee",
                    "id": employee_id,
                }
            }
        else:
            response = {
                'error': {
                    'code': 404,
                    'message': 'Employee not founded'
                }
            }

        return response
