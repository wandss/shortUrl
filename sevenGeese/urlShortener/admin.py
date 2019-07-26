from django.contrib import admin

from .models import Urls


class UrlsAdmin(admin.ModelAdmin):

    fields = ['normal_url']

admin.site.register(Urls, UrlsAdmin)
