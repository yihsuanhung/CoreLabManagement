from import_export import resources
from .models import Person

class PersonResource(resources.ModelResource):
    class Meta:
        model = Person
        #exclude = ("name","extension","number","phone","mail","alt_mail","job_title","organization","employee_ID","access_card","core_lab","role",)
        import_id_fields = ['uid']
