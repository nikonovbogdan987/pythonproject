from django.db import models

# Create your models here.
class Clients(models.Model):
    name = models.CharField("Имя", max_length=50)
    surname = models.CharField("Фамилия",max_length=50)
    email = models.EmailField("Эл.почта", max_length=50)
    phone = models.CharField("Телефон", max_length=11)
    password = models.CharField("Пароль", max_length=20)

    def __str__(self) -> str:
        return self.name

    # переименование в админ-панели название таблицы
    class Meta:
        verbose_name = "клиента"
        verbose_name_plural = "Клиенты"
class Orders(models.Model):
    author = models.ForeignKey(Clients, on_delete=models.CASCADE)
    data = models.DateField("Дата заказа")
    name_game = models.CharField("Название игры", max_length=50)
    price = models.IntegerField("Цена игры")
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = "заказ"
        verbose_name_plural = "Заказы"

