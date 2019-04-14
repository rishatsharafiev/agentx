from django.urls import path

from .views import EmployeeView, LocationView


urlpatterns = (
    path('employee/', EmployeeView.as_view(), name='employee-create'),
    path('employee/<int:pk>/', EmployeeView.as_view(), name='employee-get-update-delete'),
    path('employee/<int:pk>/history/', LocationView.as_view(), name='location-history'),
    path('employee/<int:pk>/generate/', LocationView.as_view(), name='location-generate'),
)
