from functools import wraps
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.settings import api_settings

def cache_response(timeout=60 * 15, cache_key_prefix='', invalidate_cache=False):
    """
    Decorator to cache the response of a Django REST framework view function.

    Parameters:
    - timeout (int): The duration in seconds for which the response should be cached. Default is 15 minutes (900 seconds).
    - cache_key_prefix (str): A prefix to be added to the cache key. Default is an empty string.
    - invalidate_cache (bool): Whether to invalidate the cache before returning the response. Default is False.

    Usage:
    Apply this decorator to a view function to cache its response. If the same request is made
    again within the specified timeout period, the cached response will be returned instead of
    re-generating the response.

    Example:
    @cache_response(timeout=60 * 30, cache_key_prefix='my_view:', invalidate_cache=False)
    def my_view(request):
        # View logic here
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            cache_key = f"{cache_key_prefix}{request.get_full_path()}"

            if invalidate_cache:
                cache.delete(cache_key)
            
            cached_response = cache.get(cache_key)

            if cached_response is not None:
                print(f"Cache hit: {cache_key}")
                return Response(cached_response)

            response = view_func(request, *args, **kwargs)

            if isinstance(response, Response):
                response.accepted_renderer = api_settings.DEFAULT_RENDERER_CLASSES[0]()
                response.accepted_media_type = response.accepted_renderer.media_type
                response.renderer_context = {
                    'request': request,
                    'response': response
                }
                response.render() 
                cache.set(cache_key, response.data, timeout=timeout)
                print(f"Cache set: {cache_key} with data: {response.data}")

            return response

        return _wrapped_view
    return decorator
