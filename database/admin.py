from django.contrib import admin
from .models import PI, Staff, Card, Person
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
#admin.site.register(Person)
#admin.site.register(PI)
#admin.site.register(Staff)
#admin.site.register(Card)

#https://django-import-export.readthedocs.io/en/latest/getting_started.html
class PersonResource(resources.ModelResource):
    class Meta:
        model = Person

# @admin.register(Person)
# class PersonAdmin(ImportExportModelAdmin):
#     list = [field.name for field in Person._meta.fields if field.name != "uid"]
#     list_display  = list
#     search_fields = list
