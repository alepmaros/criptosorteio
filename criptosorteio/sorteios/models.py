import shortuuid

from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone

def gen_shortuuid():
    uuid = shortuuid.uuid()
    while Sorteio.objects.filter(id=uuid).exists():
        uuid = shortuuid.uuid()
    
    return uuid

# Create your models here.
class Sorteio(models.Model):
    """
    Modelo de um sorteio especifico.
    """
    id = models.CharField(max_length=22, default=gen_shortuuid, primary_key=True)

    nome = models.CharField(max_length=128)
    descricao = models.TextField(max_length=4096)
    foto = models.ImageField(blank=True, null=True, upload_to='sorteio/fotos/')
    
    hora_criado = models.DateTimeField(default=timezone.now, blank=False, null=False)
    hora_sorteio = models.DateTimeField(blank=False, null=False)
    string_nist = models.CharField(max_length=128, blank=True, null=True)

    criador = models.ForeignKey(User, blank=False, null=False, related_name='criador')
    ganhador = models.ForeignKey(User, null=True, blank=True, related_name='ganhador')
    participantes = models.ManyToManyField(User, blank=True, through='Participacao', related_name='participantes')

    sorteado = models.BooleanField(default=False)

    PRIVACIDADE_TIPOS = (
        ('nli', 'Não Listado'),
        ('pub', 'Publico'),
    )

    privacidade = models.CharField(max_length=3, choices=PRIVACIDADE_TIPOS, blank=False, default='nli')

    @property
    def precisa_sortear(self):
        if not self.sorteado and timezone.now() > self.hora_sorteio:
            return True
        return False

    def __str__(self):
        """
        String que representa o modelo do Sorteio
        """
        return '%s - %s - %s' % (self.pk, self.hora_sorteio, self.nome[:24])

    class Meta:
        ordering = ["hora_sorteio"]

class Participacao(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sorteio = models.ForeignKey(Sorteio, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(default=timezone.now, blank=False, null=False)

class Comentario(models.Model):
    """
    Modelo de um comentario
    """

    sorteio = models.ForeignKey(Sorteio, blank=False, null=False)
    comentador = models.ForeignKey(User, blank=False, null=False)
    comentario = models.TextField(max_length=2048, blank=False, null=False)

    def __str__(self):
        """
        String que representa o modelo do Comentario
        """

        return '%s - %s: %s' % (self.sorteio.nome[:24], self.comentador.username, self.comentario )

    def display_nome(self):
        """
        Retorna o nome do usuario do comentario
        """

        return self.comentador.username

    def display_nome_sorteio(self):
        """
        Retorna o nome do sorteio do comentario
        """

        return self.sorteio.nome