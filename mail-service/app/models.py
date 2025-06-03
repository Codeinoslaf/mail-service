from django.db import models

class EmailTask(models.Model):
    recipients = models.TextField(help_text="Список email через запятую")
    subject = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')
    
    def __str__(self):
        return f"Email to {self.recipients} - {self.subject}"