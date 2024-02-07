from django.forms import ModelForm
from apps.prestamos.models import Prestamo

class PrestamoForm(ModelForm):
    class Meta:
        model = Prestamo
        fields = ['fecha_prestamo', 'cliente', 'valor_prestamo', 'fecha_inicio_descuento', 'numero_cuotas', 'estado']
        labels = {
            'fecha_prestamo': 'Fecha del prestamo',
            'cliente': 'Nombre del cliente',
            'valor_prestamo': 'Valor del prestamo',
            'fecha_inicio_descuento': 'Fecha de inicio del descuento',
            'numero_cuotas': 'Numero de cuotas',
            'estado': 'Estado del prestamo',
        }