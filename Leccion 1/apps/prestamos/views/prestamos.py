from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from apps.prestamos.models import Prestamo
from django.urls import reverse_lazy
from apps.prestamos.forms.prestamo import PrestamoForm
from django.db.models import Q

class PrestamoListView(ListView):
    model = Prestamo
    template_name = 'prestamos/list.html'
    context_object_name = 'prestamos'
    paginate_by = 10
    
    def get_queryset(self):
        self.query=Q()
        q1 = self.request.GET.get('q1')
        if q1 is not None:
            self.query.add(Q(cliente__icontains=q1), Q.AND) 
        return self.model.objects.filter(self.query).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de prestamos'
        context['create_url'] = reverse_lazy('prestamos:prestamo_create')
        return context
    
class PrestamoCreateView(CreateView):
    model = Prestamo
    template_name = 'prestamos/form.html'
    form_class = PrestamoForm
    success_url = reverse_lazy('prestamos:prestamo_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ingresar nuevo prestamo'
        context['grabar'] = 'Grabar prestamo'
        context['back_url'] = self.success_url
        return context
    
class PrestamoUpdateView(UpdateView):
    model = Prestamo
    template_name = 'prestamos/form.html'
    form_class = PrestamoForm
    success_url = reverse_lazy('prestamos:prestamo_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Actualizar el prestamo'
        context['grabar'] = 'Actualizar prestamo'
        context['back_url'] = self.success_url
        return context
    
class PrestamoDeleteView(DeleteView):
    model = Prestamo
    template_name = 'prestamos/delete.html'
    success_url = reverse_lazy('prestamos:prestamo_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Eliminar el prestamo'
        context['grabar'] = 'Eliminar prestamo'
        context['description'] = f"¿Desea Eliminar El prestamo: {self.object.cliente}?"
        context['back_url'] = self.success_url
        return context