"""
Seed Church Structure

This management command loads the core organizational structure
used by Life Church.

The command is idempotent and can be executed multiple times
without creating duplicate records.

Usage:
    python manage.py seed_church_structure

Data Loaded:
    - Life Stage Groups
    - Ministries
    - Departments
    - Family Groups

Author:
    Life Church Backend Team
"""

from typing import Any

from django.core.management.base import BaseCommand

from church_groups.models import (
    Department,
    FamilyGroup,
    LifeStageGroup,
    Ministry,
)


class Command(BaseCommand):
    """
    Seed church organizational structure.

    This command creates the foundational church structures
    required by the assimilation engine and membership system.
    """

    help = "Load Life Church organizational structure."

    def handle(self, *args: Any, **options: Any) -> None:
        """
        Command entry point.
        """

        self.stdout.write(
            self.style.SUCCESS(
                "\nStarting church structure seeding...\n"
            )
        )

        self.seed_life_stage_groups()
        self.seed_ministries()
        self.seed_departments()
        self.seed_family_groups()

        self.stdout.write(
            self.style.SUCCESS(
                "\nChurch structure seeding completed successfully."
            )
        )

    def seed_life_stage_groups(self) -> None:
        """
        Seed Life Stage Groups.

        Life Church Rules:

        Men:
            - Junior Tribe (19-29)
            - Bridge Tribe (30-39)
            - Seniors Tribe (40+)

        Women:
            - Band A (19-29)
            - Band B (30-39)
            - Band C (40+)
        """

        groups = [
            ("Junior Tribe", "M", 19, 29),
            ("Bridge Tribe", "M", 30, 39),
            ("Seniors Tribe", "M", 40, None),
            ("Band A", "F", 19, 29),
            ("Band B", "F", 30, 39),
            ("Band C", "F", 40, None),
        ]

        for name, gender, min_age, max_age in groups:
            LifeStageGroup.objects.get_or_create(
                name=name,
                defaults={
                    "gender": gender,
                    "min_age": min_age,
                    "max_age": max_age,
                    "active": True,
                },
            )

        self.stdout.write(
            self.style.SUCCESS("✓ Life Stage Groups seeded")
        )

    def seed_ministries(self) -> None:
        """
        Seed Ministries.
        """

        ministries = [
            "Destiny Professionals Network",
            "Destiny Business Network",
            "Destiny Voices Ministry",
            "Intercessory Ministry",
            "Destiny Kids Ministry",
            "Vault Ministry",
            "FORT Ministry",
            "Rubies Ministry",
            "Life Couples",
            "Hadassah Ministry",
            "Kings and Priests Ministry",
        ]

        for ministry_name in ministries:
            Ministry.objects.get_or_create(
                name=ministry_name,
                defaults={
                    "active": True,
                },
            )

        self.stdout.write(
            self.style.SUCCESS("✓ Ministries seeded")
        )

    def seed_departments(self) -> None:
        """
        Seed Departments.
        """

        departments = [
            "ICT Department",
            "Security Department",
            "Technical Department",
            "Media Department",
            "Ushering Department",
            "Administration & Finance",
        ]

        for department_name in departments:
            Department.objects.get_or_create(
                name=department_name,
                defaults={
                    "active": True,
                },
            )

        self.stdout.write(
            self.style.SUCCESS("✓ Departments seeded")
        )

    def seed_family_groups(self) -> None:
        """
        Seed initial Family Groups.

        Additional Family Groups can be added as the
        church structure evolves.
        """

        family_groups = [
            ("FG002", "Shiloh", "Limuru"),
            ("FG004", "Zealous For Christ", "Limuru"),
            ("FG005", "Bereans", "Limuru"),
            ("FG006", "Chemchemi", "Rironi"),
            ("FG007", "Christians in Action", "Regional"),
            ("FG008", "Dominion", "Karanjee"),
            ("FG017", "Zion Family", "Limuru"),
            ("FG020", "Peniel", "Kamandura"),
            ("FG025", "Come Up Hither", "Waiyaki Way"),
            ("FG026", "The Balm of Gilead", "Kikuyu"),
            ("FG027", "Dimensions", "Kikuyu"),
            ("FG039", "Devoted", "Banana"),
            ("FG040", "Lighthouse", "Ruaka"),
            ("FG041", "Phaneroo", "Ndenderu"),
            ("FG042", "Washindi", "Kiambu"),
            ("FG043", "Oasis of Favor", "Ruiru"),
            ("FG044", "New Breed", "Kasarani"),
        ]

        for code, name, location in family_groups:
            FamilyGroup.objects.get_or_create(
                code=code,
                defaults={
                    "name": name,
                    "location": location,
                    "active": True,
                },
            )

        self.stdout.write(
            self.style.SUCCESS("✓ Family Groups seeded")
        )