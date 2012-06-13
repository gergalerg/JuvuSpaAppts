from django.contrib import admin
from juvume.look.models import Spa, Procedure, Amenities


class AmenitiesInline(admin.TabularInline):
    model = Amenities.spa.through
    extra = 1

class SpaAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'zip_code')
    search_fields = ('name', )
    inlines = [
            AmenitiesInline,
            ]

class ProcedureAdmin(admin.ModelAdmin):
    list_display = ('procedure', 'spa', 'price')
    search_fields = ('procedure', )

class AmenitiesAdmin(admin.ModelAdmin):
    search_fields = ('amenities',)
    list_filter = ('spa',)









admin.site.register(Spa, SpaAdmin)
admin.site.register(Procedure, ProcedureAdmin)
admin.site.register(Amenities, AmenitiesAdmin)
