from django.db import models


class FamilyGroup(models.Model):
    code = models.CharField(max_length=20, unique=True)

    name = models.CharField(max_length=100)

    location = models.CharField(max_length=100)

    description = models.TextField(blank=True)

    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.code} - {self.name}"


class LifeStageGroup(models.Model):

    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
    )

    name = models.CharField(max_length=100)

    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES
    )

    min_age = models.PositiveIntegerField()

    max_age = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Ministry(models.Model):

    name = models.CharField(max_length=100)

    description = models.TextField(blank=True)

    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Department(models.Model):

    name = models.CharField(max_length=100)

    description = models.TextField(blank=True)

    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name