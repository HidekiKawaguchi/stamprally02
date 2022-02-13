# Register your models here.
from django.contrib import admin
from django.contrib.gis import admin as geoadmin

from . import models

# Border
admin.site.register(models.Border, geoadmin.OSMGeoAdmin)
