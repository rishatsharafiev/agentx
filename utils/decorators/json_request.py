import json
from functools import wraps


def json_request(f):
    """Return the request as json"""
    @wraps(f)
    def wrapped(self, request, *args, **kwargs):
        """Wrapped function"""
        if request.method in ['POST', 'PUT', 'PATCH']:
            try:
                request.json = json.loads(request.body.decode('utf-8'))
            except json.JSONDecodeError:
                request.json = None
        else:
            request.json = None
        return f(self, request, *args, **kwargs)
    return wrapped
