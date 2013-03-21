from django.contrib import admin
from juvu.booking.models import Spa, Procedure, Availability

class SpaAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city')
    search_fields = ('name',)

class ProcedureAdmin(admin.ModelAdmin):
    list_display = ('procedure', 'spa', 'price')
    search_fields = ('procedure',)
    list_filter = ('spa',)

class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ('procedure', 'Availability', 'spa')
    list_filter = ('Availability',)

admin.site.register(Spa, SpaAdmin)
admin.site.register(Procedure, ProcedureAdmin)
admin.site.register(Availability, AvailabilityAdmin)
