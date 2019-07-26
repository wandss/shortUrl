from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from graphene_django.views import GraphQLView

from urlShortener.views import short_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    url(r'^(?P<short_url>7gs\.\w{1,})$', short_url),
]
