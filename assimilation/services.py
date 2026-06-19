"""
Assimilation Services

Contains business logic responsible for automatically assigning
members and visitors to the correct church structures.

Current Responsibilities:
- Age calculation
- Life Stage Group assignment
- Life Couples Ministry assignment

Future Responsibilities:
- Family Group assignment
- Department recommendations
- Ministry recommendations
- Visitor follow-up assignment
"""

from datetime import date
from typing import Optional

from church_groups.models import LifeStageGroup, Ministry
from members.models import Member


def calculate_age(date_of_birth: date | None) -> Optional[int]:
    """
    Calculate age from date of birth.

    Args:
        date_of_birth: Member's date of birth.

    Returns:
        Age in years or None if no date of birth is supplied.
    """
    if not date_of_birth:
        return None

    today = date.today()

    return (
        today.year
        - date_of_birth.year
        - (
            (today.month, today.day)
            < (date_of_birth.month, date_of_birth.day)
        )
    )


def assign_life_stage_group(member: Member) -> Optional[LifeStageGroup]:
    """
    Assign a Life Stage Group based on age and gender.

    Life Church Rules:

    Male:
        19-29 -> Junior Tribe
        30-39 -> Bridge Tribe
        40+   -> Seniors Tribe

    Female:
        19-29 -> Band A
        30-39 -> Band B
        40+   -> Band C

    Args:
        member: Member being processed.

    Returns:
        Assigned LifeStageGroup or None.
    """
    age = calculate_age(member.date_of_birth)

    if age is None:
        return None

    groups = LifeStageGroup.objects.filter(
        gender=member.gender,
        active=True,
    )

    for group in groups:
        max_age = group.max_age or 999

        if group.min_age <= age <= max_age:
            member.life_stage_group = group
            member.save(update_fields=["life_stage_group"])

            return group

    return None


def assign_life_couples_ministry(member: Member) -> Optional[Ministry]:
    """
    Automatically assign Life Couples ministry.

    Life Church Rule:
    Every married member belongs to Life Couples Ministry.

    Args:
        member: Member being processed.

    Returns:
        Assigned ministry or None.
    """
    if member.marital_status != "MARRIED":
        return None

    ministry = Ministry.objects.filter(
        name__iexact="Life Couples"
    ).first()

    if ministry:
        member.ministries.add(ministry)

    return ministry