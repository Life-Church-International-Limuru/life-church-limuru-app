from django.db import models
from django.conf import settings


class Member(models.Model):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    MARITAL_STATUS_CHOICES = (
        ('SINGLE', 'Single'),
        ('MARRIED', 'Married'),
        ('DIVORCED', 'Divorced'),
        ('WIDOWED', 'Widowed'),
    )

    MEMBERSHIP_STATUS_CHOICES = (
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
        ('TRANSFERRED', 'Transferred'),
        ('DECEASED', 'Deceased'),
    )

    MEMBERSHIP_SOURCE_CHOICES = (
        ('LEGACY', 'Legacy Import'),
        ('VISITOR', 'Visitor Conversion'),
        ('DIRECT', 'Direct Registration'),
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    member_number = models.CharField(
        max_length=20,
        unique=True
    )

    full_name = models.CharField(
        max_length=255
    )

    phone_number = models.CharField(
        max_length=20,
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True
    )

    address = models.CharField(
        max_length=255,
        blank=True
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    marital_status = models.CharField(
        max_length=20,
        choices=MARITAL_STATUS_CHOICES,
        blank=True
    )

    occupation = models.CharField(
        max_length=100,
        blank=True
    )

    date_joined_church = models.DateField(
        null=True,
        blank=True
    )

    baptized = models.BooleanField(
        default=False
    )

    emergency_contact_name = models.CharField(
        max_length=255,
        blank=True
    )

    emergency_contact_phone = models.CharField(
        max_length=20,
        blank=True
    )

    membership_status = models.CharField(
        max_length=20,
        choices=MEMBERSHIP_STATUS_CHOICES,
        default='ACTIVE'
    )

    membership_source = models.CharField(
        max_length=20,
        choices=MEMBERSHIP_SOURCE_CHOICES,
        default='LEGACY'
    )

    active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.member_number} - {self.full_name}"