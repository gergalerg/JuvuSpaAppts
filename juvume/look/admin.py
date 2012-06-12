from django.contrib import admin
from juvume.look.models import Spa, Treatment, Amenities


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








admin.site.register(Spa, SpaAdmin)
admin.site.register(Treatment, TreatmentAdmin)
admin.site.register(Amenities, AmenitiesAdmin)
