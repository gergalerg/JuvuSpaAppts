from django.contrib import admin
from juvume.look.models import Spa, Treatment

class SpaAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'zipcode')
    search_fields = ('name', )

class TreatmentAdmin(admin.ModelAdmin):
    list_display = ('treatment', 'spa', 'price')
    search_fields = ('treatment', )


admin.site.register(Spa, SpaAdmin)
admin.site.register(Treatment, TreatmentAdmin)
