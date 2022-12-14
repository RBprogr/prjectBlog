from django.forms import ModelForm
from comentarios.models import Comentario

class FormComentario(ModelForm):
  def clean(self):
    data = self.cleaned_data
    nome = data.get('nome_comentario')
    email = data.get('email_comentario')
    comentario = data.get('comentario')

    if len(nome) < 3:
      self.add_error('nome_comentario', 'Nome muito curto')

  class Meta:
    model = Comentario
    fields = ('nome_comentario', 'email_comentario', 'comentario')
