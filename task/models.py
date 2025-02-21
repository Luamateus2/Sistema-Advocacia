from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('The email field is required')
        if not name:
            raise ValueError('The name field is required')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        user = self.create_user(email, name, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=100, unique=True, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    groups = models.ManyToManyField(Group, related_name='user_groups')
    user_permissions = models.ManyToManyField(
        Permission, related_name='user_user_permissions')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    cpf = models.CharField(max_length=14, unique=True, blank=False, null=False, db_index=True)
    rg = models.CharField(max_length=9, unique=True, blank=False, null=False)
    birth_date = models.DateField()
    contact = models.CharField(max_length=14, blank=False, null=False)
    email = models.EmailField(max_length=100, unique=True)
    gender = models.CharField(max_length=50, blank=False, null=False)
    whatsapp = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=12, blank=False, null=False)
    street = models.CharField(max_length=50, blank=False, null=False)
    house_number = models.IntegerField()
    neighborhood = models.CharField(max_length=50, blank=False, null=False)
    pis = models.CharField(max_length=20, unique=True)
    series = models.CharField(max_length=20)
    state = models.CharField(max_length=2, blank=False, null=False)
    ctps_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    def clean(self):
        if not validate_email(self.email):
            raise ValidationError(
                {'email': 'The provided email address is not valid.'})

        if self.birth_date > timezone.now().date():
            raise ValidationError(
                {'birth_date': 'The birth date cannot be in the future.'})


class Case(models.Model):
    case_number = models.CharField(
        max_length=100, unique=True, blank=False, null=False)
    plaintiff = models.ForeignKey(Client, on_delete=models.PROTECT, to_field='cpf', db_column='cpf_plaintiff')
    defendant = models.CharField(max_length=100, blank=False, null=False)
    instance = models.CharField(max_length=100, blank=False, null=False)
    forum = models.CharField(max_length=100, blank=False, null=False)
    claim_value = models.CharField(
        max_length=10, blank=False, null=False)
    subject = models.CharField(max_length=500, blank=False, null=False)

    def __str__(self):
        return self.case_number


class Task(models.Model):
    task_title = models.CharField(max_length=100, unique=True, blank=False, null=False)
    base_date = models.DateField(auto_now_add=True)
    deadline = models.DateField()
    start_date = models.DateField()
    status = models.CharField(max_length=100, blank=False, null=False)
    responsible = models.CharField(max_length=100, unique=True, blank=False, null=False)
    case = models.ForeignKey(Case, on_delete=models.PROTECT, to_field='case_number', db_column='case_number')

    def __str__(self):
        return self.task_title
