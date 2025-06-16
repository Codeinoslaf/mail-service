from django.db import models


class Recipient(models.Model):
    address = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Получатель'
        verbose_name_plural = 'Получатели'

    def __str__(self):
        return self.address

class Status(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.name


class Task(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return f"{self.subject} от {self.created_at} "


class Email(models.Model):
    recipient_list = models.ManyToManyField(Recipient, related_name="recipients")
    send_at = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(Status, null=True, blank=True, on_delete=models.SET_NULL)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return f"Почтовое письмо отправлено на: {[recipient.address + " " for recipient in self.recipient_list.all()]}"

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'