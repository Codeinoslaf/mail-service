from django.db import models

# Create your models here.

class Statuses(models.Model):
    name = models.CharField(max_length=250, verbose_name="Состояние")

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

class Email(models.Model):
    subject = models.CharField(max_length=250, verbose_name="Наименование")
    body = models.CharField(max_length=250, verbose_name="Содержание")
    create_at = models.DateField(null=True, blank=True)
    statuses = models.ForeignKey(Statuses, on_delete = models.CASCADE, verbose_name="Статутс")

    def __str__(self):
        return "{}\n{}\n Дата отправки: {}".format(self.subject, self.body, self.create_At)

    class Meta:
        verbose_name = "Сообщение об отправке"
        verbose_name_plural = "Сообщения об отправке"

