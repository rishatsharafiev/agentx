from functools import wraps

from django.http import JsonResponse


def json_response(f):
    """Return the response as json"""
    @wraps(f)
    def wrapped(*args, **kwargs):
        """Wrapped function"""
        result = f(*args, **kwargs)
        response = JsonResponse(result)
        if type(result) == dict:
            if 'error' in result:
                try:
                    response.status_code = int(result.get('error', {}).get('code'))
                except ValueError:
                    result['error']['code'] = 500
                    response = JsonResponse(result)
                    response.status_code = 500
        return response
    return wrapped
