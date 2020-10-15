from django.db import models


class App(models.Model):
    id = models.CharField(null=False, blank=False, max_length=256, primary_key=True)
    secret = models.CharField(null=False, blank=False, max_length=512)
    is_internal = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return f'{self.id}'
