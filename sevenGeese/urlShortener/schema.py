import re
from uuid import uuid4

import graphene
from graphene_django.types import DjangoObjectType

from django.core.cache import cache
from .utils import create_short_url


class UrlType(graphene.ObjectType):
    short_url = graphene.String()


class Query(graphene.ObjectType):
    """Get a list of urls or filter by fields short_url
    or normal_url.
    Case a normal_url doesn't exists, it will be created.
    """
    urls = graphene.Field(UrlType, url=graphene.String())

    # def resolve_urls(self, info, **kwargs):
    #     return Urls.objects.all()

    def resolve_urls(self, info, **kwargs):
        url = kwargs.get('url')
        url_type = UrlType()

        if not url:
            return url_type

        if not re.findall('^http(s)?://+', url.lower()):
            url = "http://{}".format(url)

        if not cache.get(url):
            id = uuid4()
            url_type.normal_url = url
            url_type.short_url = create_short_url(id.fields[1])
            cache.set(url, url_type.short_url)

        else:
            url_type.short_url = cache.get(url)


        return url_type

        #if Urls.objects.filter(short_url__endswith=url).exists():
        #    return Urls.objects.filter(short_url__endswith=url).last()

        #elif Urls.objects.filter(normal_url__endswith=url).exists():
        #    return Urls.objects.filter(normal_url__endswith=url).last()

        # elif not re.findall('^7gs+', url):
        #     if not re.findall('^http(s)?://+', url.lower()):
        #         url = "http://{}".format(url)

        #     new_url = Urls.objects.create(normal_url=url)
        #     new_url.save()
        #     return new_url

#class CreateUrl(graphene.Mutation):
#
#    class Arguments:
#        url = graphene.String(required=True)
#
#    url = graphene.Field(UrlsType)
#
#    def mutate(self, info, url):
#        if not re.findall('^http(s)?://+', url.lower()):
#            url = "http://{}".format(url)
#
#        import pdb; pdb.set_trace()  #DEBUG
#
#        return CreateUrl(url=instance)
#
#
#class Mutation(graphene.ObjectType):
#    create_url = CreateUrl.Field()
