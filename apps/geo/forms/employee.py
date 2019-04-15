from django.forms import ModelForm

from ..models import Employee


class EmployeeForm(ModelForm):
    """Employee Form"""

    class Meta:
        """Meta Class"""

        model = Employee
        fields = ['first_name', 'last_name', 'gender', 'birth_day', 'email']
