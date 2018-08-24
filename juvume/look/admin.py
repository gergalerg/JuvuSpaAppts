from django.contrib import admin
from look.models import Spa, Procedure, Availability, Category


class SpaAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city')
    search_fields = ('name', )

class ProcedureAdmin(admin.ModelAdmin):
    list_display = ('procedure', 'category', 'spa', 'price')
    search_fields = ('procedure', )
    list_filter = ('spa',)

class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ('procedure', 'appt_date', 'spa',
            'timeslot', 'duration', 'status', 'base_price', 'proc_name',
            'create_date', 'staff_id')
    list_filter = ('procedure',)

class CategoryAdmin(admin.ModelAdmin):

    list_display = ('category',)
    list_filter = ('category',)

admin.site.register(Spa, SpaAdmin)
admin.site.register(Procedure, ProcedureAdmin)
admin.site.register(Availability, AvailabilityAdmin)
admin.site.register(Category, CategoryAdmin)
