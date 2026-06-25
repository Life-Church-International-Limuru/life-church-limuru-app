"""
Dashboard Services

Business logic for constructing the
member dashboard.
"""

from members.models import Member


def build_dashboard(member: Member) -> dict:
    """
    Build dashboard payload for the
    authenticated member.
    """

    return {
        "member": {
            "full_name": member.full_name,
            "membership_number": member.member_number,
            "membership_status": member.membership_status,
        },
        "church": {
            "family_group": (
                str(member.family_group)
                if member.family_group
                else None
            ),
            "life_stage_group": (
                str(member.life_stage_group)
                if member.life_stage_group
                else None
            ),
        },
        "quick_actions": [
            {
                "title": "Giving",
                "enabled": member.membership_status == "ACTIVE",
            },
            {
                "title": "Sermons",
                "enabled": True,
            },
            {
                "title": "Prayer Requests",
                "enabled": True,
            },
        ],
        "statistics": {
            "ministries": member.ministries.count(),
            "departments": member.departments.count(),
        },
    }