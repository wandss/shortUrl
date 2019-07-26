import re
from uuid import uuid4

from django.core.cache import cache

import graphene
from graphene_django.types import DjangoObjectType

from .utils import create_short_url


class UrlType(graphene.ObjectType):
    url = graphene.String()


class Query(graphene.ObjectType):
    """Receives an url and returns it's shorted or normal version
    """
    urls = graphene.Field(UrlType, url=graphene.String())

    def resolve_urls(self, info, **kwargs):
        url = kwargs.get('url')
        url_type = UrlType()
        keys = cache.keys('*')
        cached_url = [key for key in keys if cache.get(key) == url]

        if cached_url:
            url_type.url = cached_url[0]
            return url_type

        if not url:
            return url_type

        if not re.findall('^http(s)?://+', url.lower()):
            url = "http://{}".format(url)

        if not cache.get(url):
            id = uuid4()
            url_type.normal_url = url
            url_type.url = create_short_url(id.fields[1])
            cache.set(url, url_type.url)

        else:
            url_type.url = cache.get(url)

        return url_type
