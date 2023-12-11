""" DJANGO MODELS UTILITIES """

# DJANGO
from django.db import models

class BaseModel(models.Model):
    """
        Comparte los campos basicos con todos los modelos.
        Actua como una clase abstracta de los otros modelos. Esta clase añade
        los siguientes campos.
            + created (DateTime): Store the datetime the object was created.
            + modified (DateTime): Store the last datetime the object was modified.
    """

    created = models.DateTimeField(
        'Created at',
        auto_now_add = True,
        help_text='Fecha con la cual se creo el registro'
    )

    modified = models.DateTimeField(
        'modified at',
        auto_now = True,
        help_text='Fecha con la cual se modifico el objeto'
    )

    class Meta:
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created','-modified']
    