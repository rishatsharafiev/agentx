from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt


class BaseView(View):
    """Base View"""

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        """Dispatch method"""
        return super().dispatch(request, *args, **kwargs)
