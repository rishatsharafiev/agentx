from django.db import models


class Employee(models.Model):
    """Employee Model"""

    GENDER_CHOICE_MALE = 0
    GENDER_CHOICE_FEMALE = 1
    GENDER_CHOICES = (
        (GENDER_CHOICE_MALE, 'Мужчина'),
        (GENDER_CHOICE_FEMALE, 'Женщина'),
    )

    first_name = models.CharField(verbose_name='Название', max_length=255)
    last_name = models.CharField(verbose_name='Название', max_length=255)
    gender = models.PositiveIntegerField(verbose_name='Пол', choices=GENDER_CHOICES, null=True, blank=True)
    birth_day = models.DateField(verbose_name='Дата рождения', null=True, blank=True)
    email = models.EmailField(verbose_name='Email', max_length=255, null=True, blank=True)

    class Meta:
        """Meta"""

        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_gender_name(self):
        """Get gender name"""
        try:
            return Employee.GENDER_CHOICES[self.gender][1]
        except (IndexError, TypeError):
            return None
