from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}: {self.phone_number}"

    class Meta:
        verbose_name_plural = "Телефоны"
        verbose_name = "Телефон"
