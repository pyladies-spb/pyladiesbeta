from django.contrib import admin

from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin
from markdownx.models import MarkdownxField


class CustomFlatPageAdmin(FlatPageAdmin):
    content = MarkdownxField()


# unregister the default FlatPage admin and register CustomFlatPageAdmin.
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, CustomFlatPageAdmin)
