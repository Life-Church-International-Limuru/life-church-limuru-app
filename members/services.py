"""
Member Services

Business logic for:
- Membership approval
- Membership number generation
- Automatic church group assignment
"""

from datetime import datetime

from .models import Member

from church_groups.models import (
    LifeStageGroup,
    Ministry,
)

from .models import Member


def generate_membership_number() -> str:
    """
    Generate a unique membership number.

    Format:
        LCL-2026-00001
    """

    year = datetime.now().year

    count = (
        Member.objects.exclude(
            member_number__isnull=True
        ).count()
        + 1
    )

    return f"LCL-{year}-{count:05d}"


def approve_member(
    member: Member,
) -> Member:
    """
    Approve a pending member.

    Actions:
        1. Generate membership number.
        2. Assign life stage group.
        3. Assign Life Couples ministry.
        4. Activate membership.
    """

    if not member.member_number:
        member.member_number = (
            generate_membership_number()
        )

    assign_life_stage_group(member)

    member.membership_status = "ACTIVE"

    member.active = True

    member.save()

    assign_life_couples(member)

    return member

def assign_life_stage_group(
    member: Member,
) -> None:
    """
    Assign a member to the correct life stage group.
    """

    if member.age is None:
        return

    age = member.age

    if member.gender == "M":

        if age < 30:
            group_name = "Junior Tribe"

        elif age < 40:
            group_name = "Bridge Tribe"

        else:
            group_name = "Seniors Tribe"

    elif member.gender == "F":

        if age < 30:
            group_name = "Band A"

        elif age < 40:
            group_name = "Band B"

        else:
            group_name = "Band C"

    else:
        return

    member.life_stage_group = (
        LifeStageGroup.objects.get(
            name=group_name
        )
    )
    
    
def assign_life_couples(
    member: Member,
) -> None:
    """
    Assign married members to Life Couples.
    """

    if not member.marital_status:
        return

    if member.marital_status.upper() != "MARRIED":
        return

    ministry = (
        Ministry.objects.filter(
            name="Life Couples"
        ).first()
    )

    if ministry:
        member.ministries.add(ministry)
