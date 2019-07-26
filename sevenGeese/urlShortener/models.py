from django.db import models

from .utils import create_short_url


class Urls(models.Model):

    normal_url = models.URLField(unique=True)
    short_url = models.CharField(max_length=7, blank=True, unique=True)

    class Meta:
        verbose_name_plural = 'Urls'

    def save(self, *args, **kwargs):

        if Urls.objects.last() is None:
            key = 0
        else:
            key = Urls.objects.last().pk + 1

        self.short_url = create_short_url(key)

        super(Urls, self).save(*args, **kwargs)

    def __str__(self):
        return self.normal_url
