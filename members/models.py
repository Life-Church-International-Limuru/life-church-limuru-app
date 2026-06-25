from django.db import models
from django.conf import settings
from datetime import date

from church_groups.models import (
    FamilyGroup,
    LifeStageGroup,
    Ministry,
    Department,
)
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
    ("PENDING", "Pending Approval"),
    ("ACTIVE", "Active"),
    ("INACTIVE", "Inactive"),
    ("TRANSFERRED", "Transferred"),
    ("DECEASED", "Deceased"),
    ("REJECTED", "Rejected"),
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
    unique=True,
    blank=True,
    null=True,
    help_text=(
        "Generated automatically after membership approval."
    ),
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
        default="PENDING"
    )

    membership_source = models.CharField(
        max_length=20,
        choices=MEMBERSHIP_SOURCE_CHOICES,
        default='LEGACY'
    )

    active = models.BooleanField(
        default=True
    )

    family_group = models.ForeignKey(
        FamilyGroup,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    life_stage_group = models.ForeignKey(
        LifeStageGroup,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    ministries = models.ManyToManyField(
        Ministry,
        blank=True
    )

    departments = models.ManyToManyField(
        Department,
        blank=True
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    @property
    def age(self) -> int | None:
        """
        Calculate member age from date of birth.

        Returns:
            int: Age in years.
            None: If date of birth is not provided.
        """

        if not self.date_of_birth:
            return None

        today = date.today()

        return (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                <
                (
                    self.date_of_birth.month,
                    self.date_of_birth.day,
                )
            )
        )

    def __str__(self):
        """
        Human-readable representation of a member.
        """

        if self.member_number:
            return f"{self.member_number} - {self.full_name}"

        return self.full_name
    