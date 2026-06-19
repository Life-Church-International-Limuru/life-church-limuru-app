from django.contrib import admin
from .models import (
    FamilyGroup,
    LifeStageGroup,
    Ministry,
    Department
)


admin.site.register(FamilyGroup)
admin.site.register(LifeStageGroup)
admin.site.register(Ministry)
admin.site.register(Department)