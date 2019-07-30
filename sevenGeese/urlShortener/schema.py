import re

import graphene

from .models import Urls


class UrlsType(graphene.ObjectType):

    url = graphene.String()


class Query(graphene.ObjectType):
    """Get a list of urls or filter by fields short_url
    or normal_url.
    Case a normal_url doesn't exists, it will be created.
    """
    url = graphene.Field(UrlsType, url=graphene.String())

    def resolve_url(self, info, **kwargs):
        url = kwargs.get('url')

        if Urls.objects.filter(short_url__endswith=url).exists():
            url = Urls.objects.filter(
                short_url__endswith=url).last().normal_url
            return UrlsType(url=url)

        if Urls.objects.filter(normal_url__endswith=url).exists():
            url = Urls.objects.filter(
                normal_url__endswith=url).last().short_url
            return UrlsType(url=url)

        else:
            if not re.findall('^http(s)?://+', url.lower()):
                url = "http://{}".format(url)

            instance = Urls(normal_url=url)
            instance.save()
            return UrlsType(url=instance.short_url)

        return None
