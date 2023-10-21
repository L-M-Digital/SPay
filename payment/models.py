import uuid
from django.db import models
from django.utils.functional import cached_property
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission


class Store(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    fiscal_identification = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=25, null=True)
    email = models.EmailField(null=True)
    address = models.CharField(max_length=255, null=True)


class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    store = models.ForeignKey(Store, on_delete=models.RESTRICT)
    customer = models.CharField(max_length=255, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    customer_identification = models.CharField(max_length=25, null=True)
    card_number = models.CharField(max_length=25, null=True)

    def __str__(self):
        return f"{self.status} - {self.updated_at} - { self.amount}"

    @cached_property
    def status(self):
        return (
            self.payment_status.last().name
            if self.payment_status.last()
            else "No status"
        )

    class Meta:
        ordering = ["-updated_at"]
        db_table = "payment"
        verbose_name = "Pagamento"
        verbose_name_plural = "Pagamentos"


class PaymentStatus(models.Model):
    COMPLETED = "COMPLETED"
    CANCELED = "CANCELED"
    PAYMENT_STATUS = [
        (COMPLETED, "COMPLETED"),
        (CANCELED, "CANCELED"),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    payment = models.ForeignKey(
        Payment, on_delete=models.CASCADE, related_name="payment_status"
    )
    name = models.CharField(max_length=10, choices=PAYMENT_STATUS, default=COMPLETED)
    description = models.CharField(max_length=255, null=True)
    meta_data = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.payment} - {self.name} "

    class Meta:
        ordering = ["created_at"]
        db_table = "payment_status"
        verbose_name = "Status do pagamento"
        verbose_name_plural = "Status dos pagamentos"


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        verbose_name="groups",
        blank=True,
        help_text="The groups this user belongs to.",
        related_name="customuser_set",  # Custom related_name
        related_query_name="user",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name="user permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        related_name="customuser_set",  # Custom related_name
        related_query_name="user",
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    store = models.ForeignKey(Store, on_delete=models.RESTRICT, null=True)
    deleted_in = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True
    )
    is_deleted = models.BooleanField(null=False, default=False)
    access_request_message = models.CharField(blank=True, null=True, max_length=255)
    requested_access = models.BooleanField(null=False, default=False)

    class Meta:
        db_table = "user"
        verbose_name = "User"
        verbose_name_plural = "Users"

    objects = UserManager()
    username = None
    email = models.EmailField(("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class BaseProfileUser(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        blank=False,
    )
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    stores = models.ManyToManyField(Store, blank=False)
    all_stores = models.BooleanField(null=False, default=False)

    class Meta:
        abstract = True


class Partner(BaseProfileUser):
    class Meta:
        verbose_name = "Parceiro"
        verbose_name_plural = "Parceiros"


class Director(BaseProfileUser):
    class Meta:
        verbose_name = "Diretor"
        verbose_name_plural = "Diretores"


class Accountant(BaseProfileUser):
    class Meta:
        verbose_name = "Contador"
        verbose_name_plural = "Contadores"
