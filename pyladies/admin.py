from django.contrib import admin

from pyladies.models import (
    StoryPoint, Schedule, Publication, Resource, Partner
)


class StoryPointAdmin(admin.ModelAdmin):
    list_display = ('date', 'title')


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('date', 'title')
    list_filter = ('date',)


class PublicationAdmin(admin.ModelAdmin):
    list_display = ('date', 'source', 'title')
    list_filter = ('date', 'source')


class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title',)


class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(StoryPoint, StoryPointAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(Partner, PartnerAdmin)
