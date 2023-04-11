from django.contrib import admin
from experiences.models import Perk, Experience


@admin.register(Perk)
class PerkAdmin(admin.ModelAdmin):
    pass


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    pass
