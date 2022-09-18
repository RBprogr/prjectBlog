from django.db import models
from posts.models import Post
from django.contrib.auth.models import User

# Create your models here.
class Comentario(models.Model):
  nome_comentario = models.CharField(max_length=150, verbose_name='Nome')
  email_comentario = models.EmailField(verbose_name='E-mail')
  comentario = models.TextField(verbose_name='Comentario')
  post_comentario = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Post')
  usuario_comentario = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='usuario')
  data_comentario = models.DateField(auto_now_add=True, verbose_name='data de criação')
  publicado_comentario = models.BooleanField(default=False, verbose_name='publicado')

  def __str__(self) -> str:
    return self.nome_comentario
