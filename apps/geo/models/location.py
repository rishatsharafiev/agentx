from django.db import models

from .employee import Employee


class Location(models.Model):
    """Location Model"""

    employee = models.ForeignKey(Employee, verbose_name='Сотрудник', on_delete=models.CASCADE)
    latitude = models.DecimalField(verbose_name='Широта', max_digits=9, decimal_places=6)
    longitude = models.DecimalField(verbose_name='Долгота', max_digits=9, decimal_places=6)
    created_at = models.DateTimeField(verbose_name='Дата и время создания', auto_now_add=True)

    class Meta:
        """Meta"""

        verbose_name = 'Координата'
        verbose_name_plural = 'Координаты'

    def __str__(self):
        return f"{self.employee} ({self.latitude}, {self.latitude}) [{self.created_at}]"
