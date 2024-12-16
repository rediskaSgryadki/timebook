from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)
    is_archived = models.BooleanField(default=False)
    def __str__(self):
        return f"Note {self.title} by {self.user.username}"
    class Meta:
        ordering = ['-created_at']  # Сортировка заметок по дате создания, начиная с последних
