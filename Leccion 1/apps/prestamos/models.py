from django.db import models
from django.forms import model_to_dict

# Create your models here.
from django.db import models
from django.forms.models import model_to_dict

class Prestamo(models.Model):
    fecha_prestamo = models.DateTimeField(null=False)
    cliente = models.CharField(max_length=150)
    valor_prestamo = models.FloatField(verbose_name="Valor del préstamo")
    fecha_inicio_descuento = models.DateTimeField(null=False)
    numero_cuotas = models.IntegerField(verbose_name="Número de cuotas")
    cuotas = models.FloatField(verbose_name="Cuotas", blank=True, null=True)
    estado = models.BooleanField(verbose_name='Activo', default=True)
    
    def save(self, *args, **kwargs):
        if self.valor_prestamo and self.numero_cuotas:
            self.cuotas = self.valor_prestamo / self.numero_cuotas
        super().save(*args, **kwargs)

    def get_model_to_dict(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Prestamo'
        verbose_name_plural = 'Prestamos'
        ordering = ['-fecha_prestamo']
