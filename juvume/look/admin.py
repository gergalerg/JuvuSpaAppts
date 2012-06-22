from django.contrib import admin
from juvume.look.models import Spa, Treatment, Amenities, Category, Procedure, Availability


class AmenitiesInline(admin.TabularInline):
    model = Amenities.spa.through
    extra = 1

class SpaAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'zip_code')
    search_fields = ('name', )
    inlines = [
            AmenitiesInline,
            ]

class TreatmentAdmin(admin.ModelAdmin):
    list_display = ('treatment', 'spa', 'price')
    search_fields = ('treatment', )

class AmenitiesAdmin(admin.ModelAdmin):
    search_fields = ('amenities',)
    list_filter = ('spa',)

class CategoryAdmin(admin.ModelAdmin):
   list_display = ('categoryname',)
    #search_fields = ('categoryname', )
    #list_filter = ('categoryName',)

class ProcedureAdmin(admin.ModelAdmin):
    list_display = ('procedure', 'spa', 'price')
    search_fields = ('procedure', )
    list_filter = ('spa',)

class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ('procedure', 'appt_date', 'spa',
            'timeslot', 'duration', 'status', 'base_price', 'proc_name',
            'create_date', 'staff_id')
    list_filter = ('procedure',)



admin.site.register(Spa, SpaAdmin)
admin.site.register(Treatment, TreatmentAdmin)
admin.site.register(Amenities, AmenitiesAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Procedure, ProcedureAdmin)
admin.site.register(Availability, AvailabilityAdmin)

