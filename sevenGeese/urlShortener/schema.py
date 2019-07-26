import re

import graphene
from graphene_django.types import DjangoObjectType

from .models import Urls
from .utils import create_short_url


class UrlsType(DjangoObjectType):

    class Meta:
        model = Urls


class Query(graphene.ObjectType):
    """Get a list of urls or filter by fields short_url
    or normal_url.
    Case a normal_url doesn't exists, it will be created.
    """
    urls = graphene.List(UrlsType)
    url = graphene.Field(UrlsType, url=graphene.String())

    def resolve_urls(self, info, **kwargs):
        return Urls.objects.all()

    def resolve_url(self, info, **kwargs):
        url = kwargs.get('url')

        if Urls.objects.filter(short_url__endswith=url).exists():
            return Urls.objects.filter(short_url__endswith=url).last()

        elif Urls.objects.filter(normal_url__endswith=url).exists():
            return Urls.objects.filter(normal_url__endswith=url).last()

        # elif not re.findall('^7gs+', url):
        #     if not re.findall('^http(s)?://+', url.lower()):
        #         url = "http://{}".format(url)

        #     new_url = Urls.objects.create(normal_url=url)
        #     new_url.save()
        #     return new_url


        return None


class CreateUrl(graphene.Mutation):

    class Arguments:
        url = graphene.String(required=True)

    url = graphene.Field(UrlsType)

    def mutate(self, info, url):
        if not re.findall('^http(s)?://+', url.lower()):
            url = "http://{}".format(url)

        instance = Urls(normal_url=url)
        instance.save()

        return CreateUrl(url=instance)


class Mutation(graphene.ObjectType):
    create_url = CreateUrl.Field()
