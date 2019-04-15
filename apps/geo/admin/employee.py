from django.contrib import admin


class EmployeeAdmin(admin.ModelAdmin):
    """Employee Admin"""

    list_display = ('id', 'first_name', 'last_name', 'gender', 'birth_day', 'email',)
    list_filter = ('gender',)
    search_fields = ('first_name', 'last_name', 'email',)
    list_per_page = 30
