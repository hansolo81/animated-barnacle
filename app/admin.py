from django.contrib import admin

from .models import Tribe, Domain, Squad, Initiative, Sprint, Member, Role, Skill, Level


class InitiativeAdmin(admin.ModelAdmin):
    list_display = ('name', 'planned_for', 'squad', 'domain')


class DomainInline(admin.TabularInline):
    model = Domain
    extra = 1


class InitiativeInline(admin.TabularInline):
    model = Initiative
    extra = 1


class TribeAdmin(admin.ModelAdmin):
    inlines = [DomainInline]


class DomainAdmin(admin.ModelAdmin):
    list_display = ('name', 'tribe')
    inlines = [InitiativeInline]


class SquadAdmin(admin.ModelAdmin):
    list_display = ('name', 'domain')
    fieldsets = [
        (None, {'fields': ['name', 'description', 'domain','color']}),
        ('Composition', {'fields': ['scrum_master', 'business_analysts', 'frontend_dev', 'backend_dev', 'qa_engineer']})
    ]


class MemberAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'role', 'level')


class SprintAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'order')


admin.site.register(Tribe, TribeAdmin)
admin.site.register(Domain, DomainAdmin)
admin.site.register(Squad, SquadAdmin)
admin.site.register(Initiative, InitiativeAdmin)
admin.site.register(Sprint, SprintAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Skill)
admin.site.register(Role)
admin.site.register(Level)
