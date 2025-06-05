from datetime import timezone
from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Task(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField(default='')
    created_at = models.DateTimeField(default=timezone)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'



class Email(models.Model):
    recipient = models.TextField(help_text="Одна почта получателя")
    send_at = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    subject = models.ForeignKey(Task, on_delete=models.CASCADE, default='')

    def __str__(self):
        return f"Почтовое письмо отправлено {self.recipient} - {self.subject}"

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


