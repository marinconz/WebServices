from django.db import models
import uuid

class Temphum(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(verbose_name='Tipo', max_length=20)
    value = models.IntegerField(verbose_name='Valor')

    latitud = models.FloatField(verbose_name='latitud', max_length=50, default=0)

    longitud = models.FloatField(verbose_name='longitud', max_length=20, default=0)

    tipo_Terreno = models.CharField(verbose_name='tipo_Terreno', max_length=20, default="none")
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


