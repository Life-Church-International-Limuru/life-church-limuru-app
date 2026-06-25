from django.contrib import admin
from django.contrib import messages

from .models import Member
from .services import approve_member


@admin.action(description="Approve selected members")
def approve_members(
    modeladmin,
    request,
    queryset,
):
    """
    Admin action used to approve
    pending membership applications.
    """

    approved_count = 0

    for member in queryset:

        if member.membership_status == "PENDING":

            approve_member(member)

            approved_count += 1

    messages.success(
        request,
        f"{approved_count} member(s) approved successfully."
    )


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    """
    Church member administration.
    """

    list_display = (
        "member_number",
        "full_name",
        "gender",
        "marital_status",
        "family_group",
        "life_stage_group",
        "membership_status",
        "active",
    )

    search_fields = (
        "member_number",
        "full_name",
        "phone_number",
        "email",
    )

    list_filter = (
        "gender",
        "marital_status",
        "membership_status",
        "active",
        "family_group",
        "life_stage_group",
    )

    filter_horizontal = (
        "ministries",
        "departments",
    )

    ordering = (
        "full_name",
    )

    actions = [
        approve_members,
    ]
    readonly_fields = (
    "member_number",
)