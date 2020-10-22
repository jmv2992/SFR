from .models import Cliente
from .forms import FormCliente
from django.views.generic.edit import FormView


# Create your views here.

class CrearCliente(FormView):
    model = Cliente
    success_url = '/'
    form_class = FormCliente
    template_name = "home.html"

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super().form_valid(form)
