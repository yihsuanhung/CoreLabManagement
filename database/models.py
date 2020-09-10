from django.db import models
import uuid
from django.contrib import admin
from django.urls import reverse
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Create your models here.
class Person(models.Model):
    core_lab_choices = (("2","2"),("3","3"),("6","6"),("7","7"),("8","8"),("9","9"))
    role_choices = (("PI","PI"),("Staff","Staff"))
    uid =          models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank = True)
    name =         models.CharField('姓名', max_length = 10) #姓名
    extension =    models.CharField('分機', max_length = 50, blank = True, null = True) #分機
    number =       models.CharField("簡碼", max_length = 20, blank = True, null = True) #簡碼
    phone =        models.CharField("手機", max_length = 50, blank = True, null = True) #手機
    mail =         models.EmailField("主要信箱", blank = True, null = True) #主要信箱
    alt_mail =     models.CharField("次要信箱", max_length = 100, blank = True, null = True) #次要信箱
    job_title =    models.CharField("職稱", max_length = 10, blank = True, null = True) #職稱
    organization = models.CharField("單位", max_length = 10, blank = True, null = True) #單位
    employee_ID =  models.CharField("員工編號", max_length = 50, blank = True, null = True) #員工編號
    access_card =  models.BooleanField("領用門禁卡", default = False) #領用門禁卡（是/否）
    core_lab =     models.CharField("共研", max_length = 1, choices = core_lab_choices, blank = True, null = True) #共研(2/3/6/7/8/9)
    role =         models.CharField("類別", max_length = 5, choices = role_choices, blank = True, null = True) #Role
    leave =        models.BooleanField("離職", default = False) #離職
    remark =       models.CharField("備註", max_length = 300, blank = True, null = True) #備註
    
    # if role == "PI":
    #     link = models.OneToOneField(PI, verbose_name="link", on_delete=models.CASCADE)
    # if role == "Staff":
    #     link = models.OneToOneField(Staff, verbose_name="link", on_delete=models.CASCADE)
    
    
    def get_absolute_url(self):
        return reverse("database:people_detail", kwargs={"uid":self.uid})

    def get_update_url(self):
        return reverse("database:update_person", kwargs={"uid":self.uid})

    def get_delete_url(self):
        return reverse("database:delete_person", kwargs={"uid":self.uid})

    def __str__(self):
        return self.name



class PI(models.Model):
    property_choices = (("醫研部","醫研部"),("固定","固定"),("流動","流動"))
    uid =                  models.OneToOneField(Person, verbose_name="姓名", on_delete=models.CASCADE) #uid
    pass_date =            models.DateField("審核通過日", blank = True, null = True) #審核通過日
    property =             models.CharField("性質", max_length = 100, choices = property_choices, blank = True, null = True) #性質（醫研部/固定/流動）
    contact =              models.ForeignKey(Person, verbose_name="聯絡窗口", related_name = "contact", on_delete=models.CASCADE, blank = True, null = True)
    culture_room =         models.BooleanField("細胞室", default = False) #使用細胞室（是/否）
    hazardous_chemicals =  models.BooleanField("危害物", default = False) #使用危害性化學品（是/否）
    toxic_chenicals =      models.BooleanField("毒化物", default = False) #使用毒化物（是/否）
    return_date =          models.DateField("歸還日", blank = True, null = True) #歸還日
    pre_extension_date =   models.CharField("前一年度展延日期", max_length = 100, blank = True, null = True) #前一年度展延日期 DateField
    pre_extension_result = models.CharField("前一年度展延結果", max_length = 100, blank = True, null = True) #前一年度展延結果
    extension_date =       models.CharField("當年度展延日期", max_length = 100, blank = True, null = True) #當年度展延日期 DateField
    extension_result =     models.CharField("當年度展延結果", max_length = 100, blank = True, null = True) #當年度展延結果

    def get_absolute_url(self):
        return reverse("database:people_detail", kwargs={"uid":self.uid_id})
    def get_update_url(self):
        return reverse("database:update_pi", kwargs={"uid":self.uid_id})
    def __str__(self):
        id = str(self.uid)
        return id


class Staff(models.Model):
    info_card_choice = ( ('已交','已交'),('未交','未交'),('不用交','不用交') )
    uid =                     models.OneToOneField(Person, verbose_name="姓名", on_delete=models.CASCADE)
    info =                    models.ForeignKey(PI, verbose_name="人事資料卡PI", on_delete=models.CASCADE, related_name="RAs", default="", blank=True, null=True)
    card =                    models.ForeignKey(PI, verbose_name="門禁卡PI", on_delete=models.CASCADE, related_name="card_RAs", default="", blank=True, null=True)
    # permanent =               models.BooleanField("常駐", default = False)
    # school =                  models.BooleanField("上課", default = False)
    culture_room =            models.BooleanField("細胞室", default = False) #細胞室（是/否）
    culture_room_start =      models.DateField("細胞室使用日期", blank=True, null=True) #細胞室使用日期
    culture_room_end =        models.DateField("細胞室停用日期", blank=True, null=True) #細胞室停用日期
    # EHS_training =            models.BooleanField("共研講習", default = False) #共研講習
    EHS_training_date =       models.DateField("共研講習日期", blank=True, null=True) #共研講習日期
    # security_training =       models.BooleanField("生安教育訓練", default = False)
    security_training_date =  models.DateField("生安教育訓練日期", blank=True, null=True) #生安教育訓練日期
    leave_date =              models.DateField("離職日期", blank=True, null=True) #離職日期
    info_card =               models.CharField("人事資料卡", max_length = 100, choices = info_card_choice, blank = True, null = True) #人事資料卡（三選一，預設是空白）

    def get_absolute_url(self):
        return reverse("database:people_detail", kwargs={"uid":self.uid_id})
    def get_update_url(self):
        return reverse("database:update_staff", kwargs={"uid":self.uid_id})
    def __str__(self):
        id = str(self.uid)
        return id



class Card(models.Model):
    uid =          models.ForeignKey(Person, verbose_name="姓名", related_name="cards", on_delete=models.CASCADE) #uid
    card_ID =      models.CharField("卡號", max_length = 20, blank=True, null=True) #卡號
    password =     models.CharField("密碼", max_length = 10, blank=True, null=True) #密碼
    id_number =    models.CharField("身份證", max_length = 10, blank=True, null=True) #身份證
    inner_code =   models.CharField("內碼", max_length = 20, blank=True, null=True) #內碼
    receipt =      models.CharField("收據號碼", max_length = 100, blank=True, null=True) #收據號碼
    serial =       models.CharField("序號", max_length = 10, blank=True, null=True) #序號
    remark =       models.CharField("備註", max_length = 300, blank=True, null=True) #備註
    card_from =    models.CharField("From", max_length = 100, blank=True, null=True)
    card_to =      models.CharField("To", max_length = 100, blank=True, null=True)
    card_receive = models.DateField("領卡日期", blank=True, null=True) #領卡日期
    card_return =  models.DateField("退卡日期", blank=True, null=True) #退卡日期

    def get_absolute_url(self):
        return reverse("database:people_detail", kwargs={"uid":self.uid_id})
    def get_update_url(self):
        return reverse("database:update_card", kwargs={"uid":self.uid_id})
    def __str__(self):
        id = str(self.uid)
        return id



# @admin.register(Person)
# class PersonAdmin(admin.ModelAdmin):
#     list = [field.name for field in Person._meta.fields if field.name != "uid"]
#     list_display  = list
#     search_fields = list
@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    list = [field.name for field in Person._meta.fields if field.name != "uid"]
    list_display  = list
    search_fields = list

@admin.register(PI)
class PIAdmin(ImportExportModelAdmin):
    list = [field.name for field in PI._meta.fields if field.name != "id"]
    list_display  = list
    search_fields = list

@admin.register(Staff)
class StaffAdmin(ImportExportModelAdmin):
    list = [field.name for field in Staff._meta.fields if field.name != "id"]
    list_display  = list
    search_fields = list

@admin.register(Card)
class CardAdmin(ImportExportModelAdmin):
    list = [field.name for field in Card._meta.fields if field.name != "id"]
    list_display  = list
    search_fields = list
