from django.db import models

# Create your models here.
class Categoria(models.Model):
  nome_cat = models.CharField(max_length=255, verbose_name='Categoria')

  def __str__(self) -> str:
    return self.nome_cat

