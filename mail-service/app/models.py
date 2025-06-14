from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Task(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'


class Email(models.Model):
    recipient_list = models.TextField(help_text="Введите почты получателей") # не список на самом деле
    send_at = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(Status, null=True, blank=True, on_delete=models.SET_NULL)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return f"Почтовое письмо отправлено на: {self.recipient_list} ---> {Status.name}"

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Recipient(models.Model):
    address = models.CharField(max_length=255)
    tasks = models.ManyToManyField(Email, related_name="recipients")

    class Meta:
        verbose_name = 'Получатель'
        verbose_name_plural = 'Получатели'