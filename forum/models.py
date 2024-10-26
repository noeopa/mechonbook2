from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Este es el campo que necesitas
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    def __str__(self):
        return self.title
    def __str__(self):
        return f"{self.author}: {self.content[:20]}"
    
class Tema(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='temas')

    def __str__(self):
        return self.title