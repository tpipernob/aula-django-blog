from tabnanny import verbose
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Post(models.Model):
    titulo = models.CharField(max_length=300)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    #conteudo = models.TextField()
    conteudo = RichTextField()
    data = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.titulo

    class Meta:
        ordering = ['-data']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'