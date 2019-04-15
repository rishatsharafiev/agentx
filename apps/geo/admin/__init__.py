"""Admin"""

from django.contrib import admin

from .employee import EmployeeAdmin
from .location import LocationAdmin

from ..models import (
    Employee,
    Location,
)

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Location, LocationAdmin)

admin.site.site_header = 'AgentX'
admin.site.site_title = 'AgentX'
admin.site.index_title = 'Панель управления'
