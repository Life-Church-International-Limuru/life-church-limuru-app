"""
Visitor Models

Represents visitors attending Life Church.

Visitors are automatically assimilated into:
- Family Groups
- Life Stage Groups
- Ministries
- Departments

before eventual conversion to full membership.
"""

from django.db import models

from church_groups.models import (
    FamilyGroup,
    LifeStageGroup,
    Ministry,
    Department,
)


class Visitor(models.Model):
    """
    Visitor record captured through:
    - QR registration
    - Reception desk registration
    - Manual admin registration
    """

    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
    )

    MARITAL_STATUS_CHOICES = (
        ("SINGLE", "Single"),
        ("MARRIED", "Married"),
        ("DIVORCED", "Divorced"),
        ("WIDOWED", "Widowed"),
    )

    FOLLOW_UP_STATUS_CHOICES = (
        ("NEW", "New"),
        ("CONTACTED", "Contacted"),
        ("ASSIGNED", "Assigned"),
        ("CONNECTED", "Connected"),
        ("CONVERTED", "Converted"),
    )

    full_name = models.CharField(max_length=255)

    phone_number = models.CharField(max_length=20)

    email = models.EmailField(blank=True)

    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    marital_status = models.CharField(
        max_length=20,
        choices=MARITAL_STATUS_CHOICES,
        blank=True,
    )

    location = models.CharField(
        max_length=255,
        blank=True,
    )

    invited_by = models.CharField(
        max_length=255,
        blank=True,
    )

    family_group = models.ForeignKey(
        FamilyGroup,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    life_stage_group = models.ForeignKey(
        LifeStageGroup,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    ministries = models.ManyToManyField(
        Ministry,
        blank=True,
    )

    departments = models.ManyToManyField(
        Department,
        blank=True,
    )

    follow_up_status = models.CharField(
        max_length=20,
        choices=FOLLOW_UP_STATUS_CHOICES,
        default="NEW",
    )

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.full_name