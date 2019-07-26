from django.shortcuts import redirect, get_object_or_404

from .models import Urls


def short_url(request, short_url):

    normal_url = get_object_or_404(Urls, short_url=short_url).normal_url
    return redirect(normal_url)
