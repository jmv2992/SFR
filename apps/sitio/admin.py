from django.contrib import admin
from .models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'empresa', 'telefono', 'fecha_publicacion', 'email', 'pk')
    list_filter = ('fecha_publicacion',)


# Register your models here.
admin.site.register(Cliente, ClienteAdmin)