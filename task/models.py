from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class UsuarioManager(BaseUserManager):
    def create_user(self, email, nome, password=None):
        if not email:
            raise ValueError('O campo email é obrigatório')
        if not nome:
            raise ValueError('O campo nome é obrigatório')

        email = self.normalize_email(email)
        user = self.model(email=email, nome=nome)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, password=None):
        user = self.create_user(email, nome, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=100, unique=True, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    groups = models.ManyToManyField(Group, related_name='usuario_groups')
    user_permissions = models.ManyToManyField(
        Permission, related_name='usuario_user_permissions')

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=50, blank=False,null=False)
    cpf = models.CharField(max_length=14, unique=True, blank=False,null=False, db_index=True)  # Adicionando o db_index
    rg = models.CharField(max_length=9, unique=True, blank=False,null=False)
    data_nascimento = models.DateField()
    contato = models.CharField(max_length=14, blank=False,null=False)
    email = models.EmailField(max_length=100, unique=True)
    genero = models.CharField(max_length=50, blank=False,  null=False)
    whatsapp = models.CharField(max_length=50)
    cep = models.CharField(max_length=12, blank=False, null=False)
    logradouro = models.CharField(max_length=50, blank=False, null=False)
    numero_casa = models.IntegerField()
    bairro = models.CharField(max_length=50, blank=False, null=False)
    pis = models.CharField(max_length=20,unique=True)
    serie = models.CharField(max_length=20)
    uf = models.CharField(max_length=2,blank=False,null=False)
    numeracao_ctps = models.CharField(max_length=10)
    
    def __str__(self):
        return self.nome 
    def clean(self):
        if not validate_email(self.email):
            raise ValidationError(
                {'email': 'O endereço de e-mail fornecido não é válido.'})

      
        if self.data_nascimento > timezone.now().date():
            raise ValidationError(
                {'data_nascimento': 'A data de nascimento não pode estar no futuro.'})


class Processo(models.Model):
    numero_processo = models.CharField(
        max_length=100, unique=True, blank=False, null=False)
    autor = models.ForeignKey(Cliente, on_delete=models.CASCADE, to_field='cpf', db_column='cpf_autor')
    reu = models.CharField(max_length=100, blank=False, null=False)
    instancia = models.CharField(max_length=100, blank=False, null=False)
    forum = models.CharField(max_length=100, blank=False, null=False)
    valor_da_causa = models.DecimalField(
        max_digits=10, decimal_places=2, blank=False, null=False)
    assunto = models.CharField(max_length=500, blank=False, null=False)
    clientes = models.ManyToManyField(Cliente, related_name='processos')

    def __str__(self):
        return self.numero_processo

    
class Tarefa(models.Model):
     titulo_tarefa = models.CharField(max_length=100,unique=True, blank=False, null=False)
     data_base = models.DateField()
     data_fatal = models.DateField()
     data_final = models.DateField()
     situacao = models.CharField(max_length=100, blank=False, null=False)
     responsavel = models.CharField(max_length=100,unique=True, blank=False, null=False)
     processo = models.ForeignKey(Processo, on_delete=models.CASCADE)
     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
     def __str__(self):
        return self.titulo_tarefa
    
class Andamento(models.Model):
    processo = models.ForeignKey(Processo, on_delete=models.CASCADE, related_name='andamentos')
    descricao =models.CharField(max_length=500, blank=False, null=False)
    status =  models.CharField(max_length=100, blank=False, null=False)
    def __str(self):
         return self.descricao