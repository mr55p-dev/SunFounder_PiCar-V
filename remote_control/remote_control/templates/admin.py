from django.contrib import admin

from remote_control.templates.models import RecordDriver


class RecordActionAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'action', 'speed')


admin.site.register(RecordDriver, RecordActionAdmin)
