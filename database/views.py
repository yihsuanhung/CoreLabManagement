from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils.http import urlquote
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.db.models import Q
from .models import PI, Staff, Card, Person
from .forms import PersonForm, PIForm, StaffForm, CardForm
import datetime, csv, codecs, io, xlsxwriter, zipfile



#################### HOME ####################
@login_required
def home(request):
    return render(request, "database/home.html")


#################### LOG ####################
@login_required
def log(request):
    return render(request, "database/log.html")


#################### SEARCH ####################
@login_required
def search(request):
    template = 'database/search.html'
    person_list = None
    pi_list     = None
    staff_list  = None

    query_time_start = request.GET.get('time_start', None)
    query_time_end   = request.GET.get('time_end', None)
    query_access_card = request.GET.get("access_card", None)
    query_culture_room = request.GET.get("culture_room", None)
    query_hazardous_chemicals = request.GET.get("hazardous_chemicals", None)
    query_toxic_chenicals = request.GET.get("toxic_chenicals", None)
    query_permanent = request.GET.get("permanent", None)
    query_culture_room_staff = request.GET.get("culture_room_staff", None)


    # Update pi_list
    if query_time_end and query_time_start is not None:
        pi_list = PI.objects.filter(
        Q(pre_extension_date__range=[query_time_start,query_time_end])
        )
        li = []
        for i in range(len(pi_list)):
            li.append(Person.objects.get(uid=pi_list[i].uid_id))
        person_list=li

    #領用門禁卡
    if query_access_card is not None:
        if query_access_card == "True":
            person_list = Person.objects.filter(access_card=True)
        elif query_access_card == "False":
            person_list = Person.objects.filter(access_card=False)
    #使用細胞室
    if query_culture_room is not None:
        if query_culture_room == "True":
            pi_list = PI.objects.filter(culture_room=True)
        elif query_culture_room == "False":
            pi_list = PI.objects.filter(culture_room=False)
        li = []
        for i in range(len(pi_list)):
            li.append(Person.objects.get(uid=pi_list[i].uid_id))
        person_list=li

    #使用危害性化學品
    if query_hazardous_chemicals is not None:
        if query_hazardous_chemicals == "True":
            pi_list = PI.objects.filter(hazardous_chemicals=True)
        elif query_hazardous_chemicals == "False":
            pi_list = PI.objects.filter(hazardous_chemicals=False)
        li = []
        for i in range(len(pi_list)):
            li.append(Person.objects.get(uid=pi_list[i].uid_id))
        person_list=li

    #使用毒化物
    if query_toxic_chenicals is not None:
        if query_toxic_chenicals == "True":
            pi_list = PI.objects.filter(toxic_chenicals=True)
        elif query_toxic_chenicals == "False":
            pi_list = PI.objects.filter(toxic_chenicals=False)
        li = []
        for i in range(len(pi_list)):
            li.append(Person.objects.get(uid=pi_list[i].uid_id))
        person_list=li

    #常駐 (助理)
    if query_permanent is not None:
        if query_permanent == "True":
            staff_list = Staff.objects.filter(permanent=True)
        elif query_permanent == "False":
            staff_list = Staff.objects.filter(permanent=False)
        li = []
        for i in range(len(staff_list)):
            li.append(Person.objects.get(uid=staff_list[i].uid_id))

            # Get pi id in staff list
            pi_id = staff_list[i].pi
            card_pi_id = staff_list[i].card_pi

            # Get pi name form pi id
            pi_name = Person.objects.get(uid=pi_id)
            # pi_link = pi_name.get_absolute_url()
            card_pi_name = Person.objects.get(uid=card_pi_id)
            # card_pi_link = card_pi_name.get_absolute_url()

            # Update pi name in objects
            staff_list[i].pi = pi_name
            staff_list[i].card_pi = card_pi_name
            # print(staff_list[i].pi.get_absolute_url())

        person_list=li
    # else:
    #     pi_link = None
    #     card_pi_link = None

    #使用細胞室 (助理)
    if query_culture_room_staff is not None:
        if query_culture_room_staff == "True":
            staff_list = Staff.objects.filter(culture_room=True)
        elif query_culture_room_staff == "False":
            staff_list = Staff.objects.filter(culture_room=False)

        li = []
        # pi_name_list = []
        for i in range(len(staff_list)):
            li.append(Person.objects.get(uid=staff_list[i].uid_id))

            # Get pi id in staff list
            pi_id = staff_list[i].pi
            card_pi_id = staff_list[i].card_pi

            # Get pi name form pi id
            pi_name = Person.objects.get(uid=pi_id)
            card_pi_name = Person.objects.get(uid=card_pi_id)

            # Update pi name in objects
            staff_list[i].pi = pi_name
            staff_list[i].card_pi = card_pi_name

        person_list=li



    date = str(datetime.date.today())
    context = {
        "person_list":person_list,
        "pi_list":pi_list,
        "staff_list":staff_list,
        "date":date,
        # 'pi_link':pi_link,
        # 'card_pi_link':card_pi_link
    }

    return render(request, template, context)



#################### BROWSE ####################
@login_required
def browse(request):
    person_list = Person.objects.all()
    template = "database/browse.html"
    context = {"person_list":person_list}
    return render(request, template, context)


@login_required
def browse_PI(request):
    Pi_list = PI.objects.all()
    
    holding_cards_list = []
    remaining_cards_list = []
    pi_list = []
    for pi in Pi_list:
        holding_cards = 0
        # 檢查pi類別
        if pi.property == "流動":
            max_card = 1
            # 檢查pi本身有沒有卡
            if pi.uid.access_card == True:
                holding_cards += 1
            # 檢查他的助理有沒有卡
            if len(pi.card_RAs.all()) != 0:
                for ra in pi.card_RAs.all():
                    if ra.uid.access_card == True and ra.card == pi and ra.uid.leave == False:
                        holding_cards += 1
            
            remaining_cards_list.append(max_card-holding_cards)
            # holding_cards_list.append(max_card-holding_cards)

        if pi.property == "固定":
            max_card = 2
            # 檢查pi本身有沒有卡
            if pi.uid.access_card == True:
                holding_cards += 1
            # 檢查他的助理有沒有卡
            if len(pi.card_RAs.all()) != 0:
                for ra in pi.card_RAs.all():
                    if ra.uid.access_card == True and ra.card == pi and ra.uid.leave == False:
                        holding_cards += 1

            remaining_cards_list.append(max_card-holding_cards)
            # holding_cards_list.append(max_card-holding_cards)

        if pi.property == "醫研部":
            max_card = 100
            # 檢查pi本身有沒有卡
            if pi.uid.access_card == True:
                holding_cards += 1
            # 檢查他的助理有沒有卡 pi.RAs & pi.card_RAs
            if len(pi.card_RAs.all()) != 0:
                for ra in pi.card_RAs.all():
                    if ra.uid.access_card == True and ra.card == pi and ra.uid.leave == False:
                        holding_cards += 1
            remaining_cards_list.append("無上限")
            # holding_cards_list.append(holding_cards)

        holding_cards_list.append(holding_cards)
        pi_list.append(pi)

    pi_list_zip_holding_cards = zip(pi_list, holding_cards_list, remaining_cards_list)
    template = "database/browse_PI.html"
    context = {
        "PI_list":Pi_list,
        "pi_list_zip_holding_cards":pi_list_zip_holding_cards
        }
    return render(request, template, context)


@login_required
def browse_staff(request):
    staff_list = Staff.objects.all()
    template = "database/browse_staff.html"
    context = {"staff_list":staff_list}
    return render(request, template, context)


@login_required
def browse_card(request):
    card_list = Card.objects.all()
    staff_list = Staff.objects.all()
    template = "database/browse_card.html"
    context = {"card_list":card_list}
    return render(request, template, context)



#################### DETAIL ####################
@login_required
def detail(request,uid):
    #Person
    try:
        people_list_detail = Person.objects.get(uid=uid)
    except:
        people_list_detail = None

    #PI
    try:
        pi = PI.objects.get(uid=uid)
        pi_uid = pi.uid_id

        #PI剩餘卡數
        ra_cards = 0
        pi_cards = 0

        # 人資卡助理
        ras = pi.RAs.all()
        ra_count = pi.RAs.count()

        # 門禁卡助理
        card_ras = pi.card_RAs.all()
        card_ra_count = pi.card_RAs.count()

        pi_property = pi.property

        card_holder = []
        if card_ra_count != 0:
            for i in range(card_ra_count):
                ra = card_ras[i]
                if ra.uid.access_card == True and ra.uid.leave != True:
                    card_holder.append(ra.uid)
                    ra_cards += 1

        mails = []
        for j in range(ra_count):
            ra = ras[j]
            mails.append(ra.uid.mail)


        if pi.uid.access_card == True:
            card_holder.append(pi.uid)
            pi_cards = 1

        cards = pi_cards + ra_cards

        remaining_cards = None
        total_cards_dmr = None
        #### 固定：上限２張
        if pi_property == '固定':
            remaining_cards = 2 - cards
        #### 流動：上限１張
        elif pi_property == '流動':
            remaining_cards = 1 - cards
        #### 醫研部：無上限
        elif pi_property == '醫研部':
            # dmr: Department of medical research
            total_cards_dmr = cards


        #聯絡方式
        # contact = []
        # if ra_count == 1:
        #     contact.append(ras[0])
        # else:
        #     for i in range(ra_count):
        #         contact.append(ras[i])
        #
        # if card_ra_count == 1:
        #     contact.append(card_ras[0])
        # else:
        #     for i in range(card_ra_count):
        #         contact.append(card_ras[i])
        #
        # contact = list(dict.fromkeys(contact))
        # contact.append(pi)


    except:
        pi = None
        card_holder = None
        remaining_cards = None
        total_cards_dmr = None
        ras = None
        mails = None
        # contact = None ########### TODO: contact


    #Staff
    try:
        staff_list_detail = Staff.objects.get(uid=uid)
    except:
        staff_list_detail = None

    #Card
    try:
        card_list_detail = Card.objects.get(uid=uid)
    except:
        card_list_detail = None

    #Context
    context = {
        'detail_people': people_list_detail,
        'detail_PI': pi,
        'detail_staff': staff_list_detail,
        'detail_card': card_list_detail,
        'remaining_cards':remaining_cards,
        'total_cards_dmr':total_cards_dmr,
        'card_holder':card_holder,
        'assistants':ras,
        'mails':mails,
        # 'contact':contact ########### TODO: contact
    }
    return render(request, 'database/detail.html',context)



#################### CREATE ####################
# @login_required
# def create_person(request):
#     form = PersonForm(request.POST or None)
#
#     if form.is_valid():
#         form.save()
#         form = PersonForm()
#
#     context = {'form' : form }
#     return render(request, "database/create_person.html", context)

@login_required
def success(request):
    return render(request, "database/create_success.html")


class PersonCreate(CreateView):
    model = Person
    fields = '__all__'
    template_name = 'database/create_person.html'
    # success_url = 'create/success'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PICreate(CreateView):
    model = PI
    fields = '__all__'
    template_name = 'database/create_pi.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class StaffCreate(CreateView):
    model = Staff
    fields = '__all__'
    template_name = 'database/create_staff.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class CardCreate(CreateView):
    model = Card
    fields = '__all__'
    template_name = 'database/create_card.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

#################### UPDATE ####################
# class PersonUpdate(UpdateView):
#     model = Person
#     fields = '__all__'
#     template_name_suffix = '_update_form'
#     pk_url_kwarg = 'uid'
#
#     @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)


@login_required
def PersonUpdate(request, uid):
    object = Person.objects.get(uid=uid)
    form = PersonForm(request.POST or None, instance=object)
    obj_url = object.get_absolute_url()

    if form.is_valid():
        object = form.save(commit=False)
        object.save()
        return HttpResponseRedirect(obj_url)

    template = "database/update_person.html"
    context = { 'form':form, 'obj_url':obj_url }
    return render(request, template, context)



@login_required
def PIUpdate(request, uid):
    object = PI.objects.get(uid=uid)
    form = PIForm(request.POST or None, instance=object)
    obj_url = object.get_absolute_url()

    if form.is_valid():
        object=form.save(commit=False)
        object.save()
        return HttpResponseRedirect(object.get_absolute_url())

    template = "database/update_pi.html"
    context = { 'form':form, 'obj_url':obj_url }
    return render(request, template, context)


@login_required
def StaffUpdate(request, uid):
    object = Staff.objects.get(uid=uid)
    form = StaffForm(request.POST or None, instance=object)
    obj_url = object.get_absolute_url()

    if form.is_valid():
        object=form.save(commit=False)
        object.save()
        return HttpResponseRedirect(object.get_absolute_url())

    template = "database/update_staff.html"
    context = { 'form':form, 'obj_url':obj_url }
    return render(request, template, context)


@login_required
def CardUpdate(request, uid):
    object = Card.objects.get(uid=uid)
    form = CardForm(request.POST or None, instance=object)
    obj_url = object.get_absolute_url()

    if form.is_valid():
        object=form.save(commit=False)
        object.save()
        return HttpResponseRedirect(object.get_absolute_url())

    template = "database/update_card.html"
    context = { 'form':form, 'obj_url':obj_url }
    return render(request, template, context)


#################### DELETE ####################
class PersonDelete(DeleteView):
    model = Person
    success_url = '/database/browse'
    template_name_suffix = '_confirm_delete'
    pk_url_kwarg = 'uid'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


#################### EXPORT ####################
# @login_required
# def backup(request):
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="%s"'%(urlquote("backup.csv"))
#     response.write(codecs.BOM_UTF8)
#
#     writer = csv.writer(response, delimiter=',')
#     writer.writerow(['姓名', '分機', '簡碼', '手機', '主要信箱', '次要信箱', '職稱', '單位', '員工編號', '領用門禁卡', '共研', '類別', '離職', '備註'])
#
#     people = Person.objects.all()
#     for person in people:
#         writer.writerow([person.name,person.extension,person.number,
#         person.phone,person.mail,person.alt_mail,person.job_title,
#         person.organization,person.employee_ID,person.access_card,
#         person.core_lab,person.role,person.leave,person.remark])
#
#     return response

@login_required
def backupall(request):
    output = io.BytesIO()  #用BytesIO 來存我們的資料
    workbook = xlsxwriter.Workbook(output)  #用xlsxwriter.Workbook來開啟我們剛剛建立的BytesIO

    # sheet1-Person
    worksheet1 = workbook.add_worksheet('基本資料')  #新增一個sheet
    row = 1
    col = 0
    person_head = ['姓名', '分機', '簡碼', '手機', '主要信箱', '次要信箱', '職稱',
    '單位', '員工編號', '領用門禁卡', '共研', '類別', '離職', '備註']

    for col in range(len(person_head)):
        worksheet1.write(0, col, person_head[col])

    people = Person.objects.all()
    for i in range(len(people)):
        worksheet1.write(row, 0, people[i].name)
        worksheet1.write(row, 1, people[i].extension)
        worksheet1.write(row, 2, people[i].number)
        worksheet1.write(row, 3, people[i].phone)
        worksheet1.write(row, 4, people[i].mail)
        worksheet1.write(row, 5, people[i].alt_mail)
        worksheet1.write(row, 6, people[i].job_title)
        worksheet1.write(row, 7, people[i].organization)
        worksheet1.write(row, 8, people[i].employee_ID)
        worksheet1.write(row, 9, people[i].access_card)
        worksheet1.write(row, 10, people[i].core_lab)
        worksheet1.write(row, 11, people[i].role)
        worksheet1.write(row, 12, people[i].leave)
        worksheet1.write(row, 13, people[i].remark)
        # worksheet1.set_row(row, None, None, {'hidden': True}) #hide the row
        row = row + 1

    # sheet2-PI
    worksheet2 = workbook.add_worksheet('PI資料')
    row = 1
    col = 0
    pi_head = ['姓名', '審核通過日', '性質', '聯絡窗口', '細胞室', '危害物', '毒化物',
    '歸還日', '前一年度展延日期', '前一年度展延結果', '當年度展延日期', '當年度展延結果', '持有卡數', '剩餘卡數']

    for col in range(len(pi_head)):
        worksheet2.write(0, col, pi_head[col])

    pis = PI.objects.all()
    for pi in pis:
        worksheet2.write(row, 0, pi.uid.name)
        #col1
        try:
            col1 = pi.pass_date.strftime('%Y-%m-%d')
            if col1 == '1900-01-01': worksheet2.write(row, 1, "")
            else: worksheet2.write(row, 1, pi.pass_date.strftime('%Y-%m-%d'))
        except:
            worksheet2.write(row, 1, "")
        #col2
        worksheet2.write(row, 2, pi.property)
        #col3
        try: worksheet2.write(row, 3, pi.contact.name)
        except: worksheet2.write(row, 3, "")
        #col4
        worksheet2.write(row, 4, pi.culture_room)
        worksheet2.write(row, 5, pi.hazardous_chemicals)
        worksheet2.write(row, 6, pi.toxic_chenicals)
        #col7
        try:
            col7 = pi.return_date.strftime('%Y-%m-%d')
            if col7 == '1900-01-01': worksheet2.write(row, 7, "")
            else: worksheet2.write(row, 7, pi.return_date.strftime('%Y-%m-%d'))
        except:
            worksheet2.write(row, 7, "")
        #col8
        worksheet2.write(row, 8, pi.pre_extension_date)
        worksheet2.write(row, 9, pi.pre_extension_result)
        worksheet2.write(row, 10, pi.extension_date)
        worksheet2.write(row, 11, pi.extension_result)


        ### 持有卡數&剩餘卡數    
        holding_cards = 0
        # 檢查pi類別
        if pi.property == "流動":
            max_card = 1
            # 檢查pi本身有沒有卡
            if pi.uid.access_card == True:
                holding_cards += 1
            # 檢查他的助理有沒有卡
            if len(pi.card_RAs.all()) != 0:
                for ra in pi.card_RAs.all():
                    if ra.uid.access_card == True and ra.card == pi and ra.uid.leave == False:
                        holding_cards += 1
            remaining_cards = max_card - holding_cards
            
        if pi.property == "固定":
            max_card = 2
            # 檢查pi本身有沒有卡
            if pi.uid.access_card == True:
                holding_cards += 1
            # 檢查他的助理有沒有卡
            if len(pi.card_RAs.all()) != 0:
                for ra in pi.card_RAs.all():
                    if ra.uid.access_card == True and ra.card == pi and ra.uid.leave == False:
                        holding_cards += 1
            remaining_cards = max_card - holding_cards

        if pi.property == "醫研部":
            max_card = "無上限"
            # 檢查pi本身有沒有卡
            if pi.uid.access_card == True:
                holding_cards += 1
            # 檢查他的助理有沒有卡
            if len(pi.card_RAs.all()) != 0:
                for ra in pi.card_RAs.all():
                    if ra.uid.access_card == True and ra.card == pi and ra.uid.leave == False:
                        holding_cards += 1
            remaining_cards = max_card

        worksheet2.write(row, 12, holding_cards)
        worksheet2.write(row, 13, remaining_cards)




        row = row + 1

    # sheet3-Staff
    worksheet3 = workbook.add_worksheet('助理資料')
    row = 1
    col = 0
    staff_head = ['姓名', '人事資料卡PI', '門禁卡PI', '細胞室', '細胞室使用日期', '細胞室停用日期',
    '共研講習日期', '生安教育訓練日期', '離職日期', '人事資料卡']

    for col in range(len(staff_head)):
        worksheet3.write(0, col, staff_head[col])

    staffs = Staff.objects.all()
    for staff in range(len(staffs)):
        worksheet3.write(row, 0, staffs[staff].uid.name)
        #col1
        try: worksheet3.write(row, 1, staffs[staff].info.uid.name)
        except: worksheet3.write(row, 1, "")
        #col2
        try: worksheet3.write(row, 2, staffs[staff].card.uid.name)
        except: worksheet3.write(row, 2, "")
        #col3
        worksheet3.write(row, 3, staffs[staff].culture_room)
        #col4
        try:
            col4 = staffs[staff].culture_room_start.strftime('%Y-%m-%d')
            if col4 == '1900-01-01': worksheet3.write(row, 4, "")
            else: worksheet3.write(row, 4, staffs[staff].culture_room_start.strftime('%Y-%m-%d'))
        except:
            worksheet3.write(row, 4, "")
        #col5
        try:
            col5 = staffs[staff].culture_room_end.strftime('%Y-%m-%d')
            if col5 == '1900-01-01': worksheet3.write(row, 5, "")
            else: worksheet3.write(row, 5, staffs[staff].culture_room_end.strftime('%Y-%m-%d'))
        except:
            worksheet3.write(row, 5, "")
        #col6
        try:
            col6 = staffs[staff].EHS_training_date.strftime('%Y-%m-%d')
            if col6 == '1900-01-01': worksheet3.write(row, 6, "")
            else: worksheet3.write(row, 6, staffs[staff].EHS_training_date.strftime('%Y-%m-%d'))
        except:
            worksheet3.write(row, 6, "")
        #col7
        try:
            col7 = staffs[staff].security_training_date.strftime('%Y-%m-%d')
            if col7 == '1900-01-01': worksheet3.write(row, 7, "")
            else: worksheet3.write(row, 7, staffs[staff].security_training_date.strftime('%Y-%m-%d'))
        except:
            worksheet3.write(row, 7, "")
        #col8
        try:
            col8 = staffs[staff].leave_date.strftime('%Y-%m-%d')
            if col8 == '1900-01-01': worksheet3.write(row, 8, "")
            else: worksheet3.write(row, 8, staffs[staff].leave_date.strftime('%Y-%m-%d'))
        except:
            worksheet3.write(row, 8, "")
        #col9
        worksheet3.write(row, 9, staffs[staff].info_card)
        row = row + 1

    # sheet4-Card
    worksheet4 = workbook.add_worksheet('門禁卡資料')  #新增一個sheet
    row = 1
    col = 0
    card_head = ['姓名', '卡號', '密碼', '身份證', '內碼', '收據號碼', '序號',
    '備註', 'From', 'To', '領卡日期', '退卡日期']

    for col in range(len(card_head)):
        worksheet4.write(0, col, card_head[col])

    cards = Card.objects.all()
    for card in range(len(cards)):
        worksheet4.write(row, 0, cards[card].uid.name)
        worksheet4.write(row, 1, cards[card].card_ID)
        worksheet4.write(row, 2, cards[card].password)
        worksheet4.write(row, 3, cards[card].id_number)
        worksheet4.write(row, 4, cards[card].inner_code)
        worksheet4.write(row, 5, cards[card].receipt)
        worksheet4.write(row, 6, cards[card].serial)
        worksheet4.write(row, 7, cards[card].remark)
        worksheet4.write(row, 8, cards[card].card_from)
        worksheet4.write(row, 9, cards[card].card_to)
        #col10
        try:
            col10 = cards[card].card_receive.strftime('%Y-%m-%d')
            if col10 == '1900-01-01': worksheet4.write(row, 10, "")
            else: worksheet4.write(row, 10, cards[card].card_receive.strftime('%Y-%m-%d'))
        except:
            worksheet4.write(row, 10, "")
        #col11
        try:
            col10 = cards[card].card_return.strftime('%Y-%m-%d')
            if col10 == '1900-01-01': worksheet4.write(row, 11, "")
            else: worksheet4.write(row, 11, cards[card].card_return.strftime('%Y-%m-%d'))
        except:
            worksheet4.write(row, 11, "")
        row = row + 1


    # worksheet1.protect('123456') 
    workbook.close()  #把workbook關閉
    output.seek(0)
    response = HttpResponse(output.read(),content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

    today = datetime.datetime.now().strftime('%Y-%m-%d')
    # filename = "人事資料備份" + today + ".xlsx"
    filename = "待加密" + today + "人事資料備份.xlsx"


    response['Content-Disposition'] = 'attachment; filename="%s"'%(urlquote(filename))
     #定義本函數對應之response為下載檔案excel.xlsx

    # response = zipfile.ZipExtFile(response)
    return response
