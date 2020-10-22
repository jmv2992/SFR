from django.urls import path
from .views import CrearCliente

urlpatterns = [
	path('', CrearCliente.as_view(), name='home'),
]