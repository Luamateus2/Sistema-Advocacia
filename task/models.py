from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.core.validators import validate_ipv4_address
from django.core.validators import validate_email
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
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
    contato = models.CharField(max_length=14, blank=False)
    email = models.EmailField(max_length=100, unique=True, blank=False)
    genero = models.CharField(max_length=50, blank=False)
    whatsapp = models.CharField(max_length=50, blank=False)
    cep = models.CharField(max_length=12, blank=False)
    logradouro = models.CharField(max_length=50, blank=False)
    numero_casa = models.IntegerField()
    bairro = models.CharField(max_length=50, blank=False)
    def __str__(self):
        return self.nome 
    def clean(self):
        if not validate_email(self.email):
            raise ValidationError(
                {'email': 'O endereço de e-mail fornecido não é válido.'})

      
        if self.data_nascimento > timezone.now().date():
            raise ValidationError(
                {'data_nascimento': 'A data de nascimento não pode estar no futuro.'})

        if self.genero not in ['masculino', 'feminino', 'outro']:
            raise ValidationError({'genero': 'Gênero inválido.'})


        if not RegexValidator(regex=r'^\d{8,14}$')(self.contato):
            raise ValidationError({'contato': 'Número de telefone inválido.'})




    