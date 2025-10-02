from django.contrib import admin
from .models.Tomo import Tomo
from .models.DetalleTomo import DetalleTomo

admin.site.register(Tomo)
admin.site.register(DetalleTomo)
