from django.db import models

# Create your models here.
class Clients(models.Model):
    name = models.CharField("ФИО", max_length=50)
    login = models.CharField("Логин",max_length=50)
    email = models.EmailField("Эл.почта", max_length=50)
    phone = models.CharField("Телефон", max_length=11)
    password = models.CharField("Пароль", max_length=20)

    def __str__(self) -> str:
        return self.name

        # переименование в админ-панели название таблицы
    class Meta:
        verbose_name = "клиента"
        verbose_name_plural = "Клиенты"