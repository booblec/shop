from django.contrib import admin

from .models import *


class AcsAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='acs'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class BagAdmin(admin.ModelAdmin):



    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='bag'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)







admin.site.register(Category)
admin.site.register(Acs)
admin.site.register(Bag)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
