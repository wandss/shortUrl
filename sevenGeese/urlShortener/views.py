from django.shortcuts import redirect, Http404
from django.core.cache import cache


def short_url(request, short_url):
    """Redirects to a url saved to cache or return 404"""
    keys = cache.keys('*')
    url = [key for key in keys if cache.get(key) == short_url]
    if url:
        return redirect(url[0])
    else:
        raise Http404
