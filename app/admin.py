from django.contrib import admin

from .models import Tribe, Domain, Squad, Initiative, Sprint


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
        (None, {'fields': ['name', 'description', 'domain']}),
        ('Composition', {'fields': ['scrum_master', 'business_analysts', 'frontend_dev', 'backend_dev', 'qa_engineer']})
    ]



admin.site.register(Tribe, TribeAdmin)
admin.site.register(Domain, DomainAdmin)
admin.site.register(Squad, SquadAdmin)
admin.site.register(Initiative, InitiativeAdmin)
admin.site.register(Sprint)
