from django.db import models

# Create your models here.

class Parroquia(models.Model):
    class Meta:
        verbose_name_plural = "Parroquias"

    opciones_tipo_parroquia = (
        ('urbana', 'Parroquia Urbana'),
        ('rural', 'Parroqua Rural'),
    )

    nombre = models.CharField("Nombre de la parroquia", max_length=40)
    tipo = models.CharField(max_length=30, choices=opciones_tipo_parroquia)

    def __str__(self):
        return "%s - %s" % (
            self.nombre,
            self.tipo
        )


class Barrio(models.Model):
    class Meta:
        verbose_name_plural = "Barrios"
    opcion_nroParques = (
        (1, 'Un parque'),
        (2, 'Dos parques'),
        (3, 'Tres parques'),
        (4, 'Cuatro parques'),
        (5, 'Cinco parques'),
        (6, 'Seis parques'),
    )
    nombre = models.CharField("Nombre del barrio", max_length=50)
    nroViviendas = models.IntegerField("Número de vivendas")
    nroParques = models.IntegerField("Número de parques", choices=opcion_nroParques)
    nroEdificios = models.IntegerField("Número de edificios")
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE,
                                  related_name="parroquias")

    def __str__(self):
        return "%s - %d - %d - %d" % (
            self.nombre,
            self.nroViviendas,
            self.nroParques,
            self.nroEdificios
        )
