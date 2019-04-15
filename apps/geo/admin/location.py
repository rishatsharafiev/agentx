from django.contrib import admin


class LocationAdmin(admin.ModelAdmin):
    """Location Admin"""

    list_display = ('id', 'employee', 'latitude', 'longitude', 'created_at',)
    search_fields = ('employee__first_name', 'employee__last_name')
    list_per_page = 30
    readonly_fields = ('created_at',)
