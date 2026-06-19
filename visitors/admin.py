"""
Visitor Administration
"""

from django.contrib import admin

from .models import Visitor


@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):

    list_display = (
        "full_name",
        "phone_number",
        "family_group",
        "life_stage_group",
        "follow_up_status",
    )

    search_fields = (
        "full_name",
        "phone_number",
        "email",
    )

    list_filter = (
        "follow_up_status",
        "gender",
        "marital_status",
        "family_group",
        "life_stage_group",
    )

    filter_horizontal = (
        "ministries",
        "departments",
    )